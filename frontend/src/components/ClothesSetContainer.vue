<template>
  <div class="clothes_set-container">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "ClothesSetContainer"
}
</script>

<style scoped>
.clothes_set-container {
  display: flex;
}
</style>