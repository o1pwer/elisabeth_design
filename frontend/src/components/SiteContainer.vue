<template>
  <div class="site-container">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "SiteContainer"
}
</script>

<style scoped>
.site-container {
  display: flex;
  flex-direction: column;
  /*position: relative;*/
  flex: 1;
}
</style>