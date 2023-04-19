import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",
    component: () =>
      import(/* webpackChunkName: "home" */ "../views/HomeView.vue"),
  },
  {
    path: "/faq",
    name: "faq",
    component: () =>
      import(/* webpackChunkName: "faq" */ "../views/FaqView.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () =>
      import(/* webpackChunkName: "login" */ "../views/LoginView.vue"),
  },
  {
    path: "/about",
    name: "about",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/SignUp",
    name: "SignUp",
    component: () =>
      import(/* webpackChunkName: "signup" */ "../views/RegisterView.vue"),
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: () =>
      import(/* webpackChunkName: "dashboard" */ "../views/DashboardView.vue"),
  },
  {
    path: "/student/dashboard",
    name: "student dashboard",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/Student/DashboardView.vue"
      ),
  },
  {
    path: "/student/profile",
    name: "student profile",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/Student/StudentProfile.vue"
      ),
  },
  {
    path: "/admin/dashboard",
    name: "admin dashboard",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/Admin/DashboardView.vue"
      ),
  },
  {
    path: "/staff/dashboard",
    name: "staff dashboard",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/Staff/DashboardView.vue"
      ),
  },
  {
    path: "/supervisor/dashboard",
    name: "supervisor dashboard",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/Supervisor/DashboardView.vue"
      ),
  },
  {
    path: "/:pathMatch(.*)*",
    name: "not-found",
    component: () =>
      import(/* webpackChunkName: "not-found" */ "../views/NotFoundView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;