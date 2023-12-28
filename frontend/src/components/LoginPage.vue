<template>
  <div class="login-container">
    <form @submit.prevent="onSubmit" class="login-form">
      <h3 class="login-header">Login</h3>
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="loginDetails.username">
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="loginDetails.password">
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginPage',
  data() {
    return {
      loginDetails: {
        username: '',
        password: ''
      }
    };
  },
  methods: {
    onSubmit() {
      // Handle the login logic here
      console.log('Login details:', this.loginDetails);
      // You might want to call an API or something similar here
    }
  }
}
</script>

<style>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-form {
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.login-header {
  margin-bottom: 0.5rem;
}
.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button[type="submit"] {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #0056b3;
}
</style>