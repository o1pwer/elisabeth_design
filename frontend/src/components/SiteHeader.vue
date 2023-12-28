<template>
  <header class="site-header">
    <div class="text-logo" @click="openMainPage"><h1>I am a woman.</h1></div>
    <LoginButton/>
  </header>
</template>

<script>
import LoginButton from "@/components/buttons/LoginButton";

export default {
  name: 'SiteHeader',
  components: {LoginButton},
  methods: {
    openMainPage() {
      this.$router.push('/');
    },
  }
}
</script>

<style scoped>
.site-header {
  /* Add your styles here */
  display: flex;
  padding: 20px;
  background-color: #f5f5f5;
}
.text-logo {
  cursor: pointer;
  padding: 1rem;
  background-color: #ffdffd;
}
</style>