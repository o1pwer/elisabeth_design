<template>
  <div>
    <form @submit.prevent="onSubmit" class="auth-form">
      <h3 class="login-header">Login</h3>
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="loginDetails.username">
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="loginDetails.password">
      </div>
      <button type="submit" class="login-submit-button">Login</button>
      <div class="register-redirect">Don't have an account? <span class="register-redirect-button">Register</span></div>
    </form>
  </div>
</template>

<script>
export default {
  name: "LoginContent",
  data() {
    return {
      loginDetails: {
        username: '',
        password: ''
      },
    };
  },
  methods: {
    onSubmit() {
      // Handle the login logic here
      this.$emit('userLogin', this.loginDetails)
      // You might want to call an API or something similar here
    }
  },
}
</script>

<style scoped>
.login-header {
  margin-bottom: 0.5rem;
}

.form-group {
  margin-bottom: 15px;
}

.auth-form {
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.register-redirect-button {
  @apply font-bold;
  cursor: pointer;
}

.login-submit-button {
  margin-bottom: 0.5rem;
}
</style>