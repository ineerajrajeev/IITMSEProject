<template>
  <header class="text-gray-600 body-font">
    <div
      class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center"
    >
      <nav class="flex lg:w-2/5 flex-wrap items-center text-base md:ml-auto">
        <a class="mr-5 hover:text-gray-900" href="/">Home</a>
        <a class="mr-5 hover:text-gray-900" href="/faq">FAQs</a>
        <a class="mr-5 hover:text-gray-900" href="/login">Login</a>
        <a class="hover:text-gray-900" href="/register">Register</a>
      </nav>
      <a
        href="/"
        class="flex order-first lg:order-none lg:w-1/5 title-font font-medium items-center text-gray-900 lg:items-center lg:justify-center mb-4 md:mb-0"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          stroke="currentColor"
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          class="w-10 h-10 text-white p-2 bg-indigo-500 rounded-full"
          viewBox="0 0 24 24"
        >
          <path
            d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"
          ></path>
        </svg>
        <span class="ml-3 text-xl"
          >IIT Madras<br />Online Degree Programme</span
        >
      </a>
      <div class="lg:w-2/5 inline-flex lg:justify-end ml-5 lg:ml-0"></div>
    </div>
  </header>
</template>

<script>
export default {
  name: "MainNavBar",
};
</script>
