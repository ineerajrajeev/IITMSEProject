from flask import Blueprint, jsonify, request, abort
from flask_login import current_user

from api import db, student_permission, staff_permission, supervisor_permission
from api.ticket.models import Ticket, Response
from api.ticket.schemas import TicketInputSchema, ResponseInputSchema, TicketSchema

ticket_module = Blueprint('ticket', __name__, url_prefix='/api/tickets')


@ticket_module.route('/create', methods=['POST'])
@student_permission.require()
def create():
    data = {k: v.strip() for k, v in request.get_json().items()}
    schema = TicketInputSchema()
    errors = schema.validate(data)

    if errors:
        # Validation Error
        abort(422, str(errors))
    else:
        ticket = Ticket(user_id=current_user.id, subject=data['subject'])
        db.session.add(ticket)
        db.session.commit()
        resp = Response(ticket_id=ticket.id,
                        user_id=current_user.id,
                        message=data['message'])
        db.session.add(resp)
        db.session.commit()
        return jsonify({'id': ticket.id,  'status': ticket.status, 'subject': ticket.subject, 'message': resp.message}), 201


@ticket_module.route('/<id>/respond', methods=['POST'])
@staff_permission.require()
def respond(id):
    data = {k: v.strip() for k, v in request.get_json().items()}
    schema = ResponseInputSchema()
    errors = schema.validate(data)

    if errors:
        # Validation Error
        abort(422, str(errors))
    else:
        ticket = Ticket.query.filter_by(id=id, status="open").first()
        if ticket:
            ticket.status = "closed"
            resp = Response(ticket_id=id,
                            user_id=current_user.id,
                            message=data['message'])
            db.session.add(ticket)
            db.session.add(resp)
            db.session.commit()
            return jsonify({'id': id, 'status': ticket.status, 'message': resp.message}), 201
        else:
            abort(422, str({'error': 'Ticket already closed'}))


@ticket_module.route('/<id>/promote', methods=['PUT'])
@supervisor_permission.require()
def promote(id):
    ticket = Ticket.query.filter_by(id=id, status="closed").first()
    if ticket:
        ticket.faqed = True
        db.session.add(ticket)
        db.session.commit()
        return jsonify({'status': 'OK', 'message': 'Ticket promoted'}), 201
    else:
        abort(
            422, str({'error': 'Ticket does not exist, or is open, or already promoted'}))

# Get the current users (Student) complete list of tickets


@student_permission.require()
@ticket_module.route('/my', methods=['GET'])
def fetch_my():
    tickets = Ticket.query.filter_by(user_id=current_user.id).all()
    tickets = [
        {
            'id': t.id,
            'subject': t.subject,
            'status': t.status,
            'created_at': t.created_at,
        }
        for t in tickets
    ]
    return tickets

# Get the current users (Student) ticket detail


@student_permission.require()
@ticket_module.route('/my/<id>', methods=['GET'])
def fetch_my_detail(id):
    ticket = Ticket.query.filter_by(user_id=current_user.id, id=id).first()
    messages = []
    for r in ticket.responses:
        messages.append(r.message)
    return jsonify({'id': ticket.id, 'subject': ticket.subject,
                    'status': ticket.status, 'messages': messages})

# Get unanswered list of unanswered tickets


@staff_permission.require()
@ticket_module.route('/open', methods=['GET'])
def fetch_open():
    tickets = Ticket.query.filter_by(status="open").all()
    response = [
        {
            'id': t.id,
            'subject': t.subject,
            'status': t.status,
            'created_at': str(t.created_at).split()[0],
        } for t in tickets
    ]
    return jsonify(response)

# Get unanswered list of closed tickets


@staff_permission.require()
@ticket_module.route('/closed', methods=['GET'])
def fetch_closed():
    tickets = Ticket.query.filter_by(status="closed").all()
    response = [
        {
            'id': t.id,
            'subject': t.subject,
            'status': t.status,
            'created_at': str(t.created_at).split()[0],
        } for t in tickets
    ]
    return jsonify(response)

# Get FAQed tickets across all users


@ticket_module.route('/faqs', methods=['GET'])
def fetch_faqs():
    faqs = Ticket.query.filter_by(status="closed", faqed=True).all()
    schema = TicketSchema()
    return schema.dump(faqs, many=True)

# Get detail of one particular FAQ


@ticket_module.route('/faqs/<id>', methods=['GET'])
def fetch_faq_detail(id):
    faq = Ticket.query.filter_by(status="closed", faqed=True, id=id).first()
    messages = []
    for r in faq.responses:
        messages.append(r.message)
    return jsonify({'id': faq.id, 'subject': faq.subject, 'messages': messages})
