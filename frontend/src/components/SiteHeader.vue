<template>
  <header class="site-header">
    <h1>I am a woman.</h1>
    <div class="login-btn">Login</div>
  </header>
</template>

<script>
export default {
  name: 'SiteHeader'
}
</script>

<style scoped>
.site-header {
  /* Add your styles here */
  display: flex;
  padding: 20px;
  background-color: #f5f5f5;
}
.login-btn {
  display: block;
  margin-left: auto;
  align-self: center;
  @apply font-bold hover:underline;
}
</style>