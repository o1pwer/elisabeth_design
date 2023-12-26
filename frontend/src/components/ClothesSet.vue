<template>
  <div class="clothes_set">
    <!-- This slot can be used to pass custom content for each clothes set -->
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'ClothesSet'
}
</script>

<style scoped>
.clothes_set {
  /* Add your styles here */
  max-width: 100%;
  border: 1px solid #ddd;
  padding: 1rem;
}

.clothes_set * {
  max-width: 100%;
}
</style>