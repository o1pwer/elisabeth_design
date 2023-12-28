<template>
  <div class="login-btn" @click="openLoginPage">
    <slot>Login</slot>
  </div>
</template>

<script>
export default {
  name: "LoginButton",
  methods: {
    openLoginPage() {
      this.$router.push('/login');
    },
  }
}
</script>

<style scoped>
.login-btn {
  display: block;
  margin-left: auto;
  align-self: center;
  padding: 0.5rem;
  outline: 1px solid black;
  border-radius: 4px;
  cursor: pointer;
  @apply font-bold hover:underline;
}
</style>