<template>
  <div class="clothes_set">
    <!-- This slot can be used to pass custom content for each clothes set -->
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'ClothesSet',
  methods: {
    test() {
      return require('../assets/media/photo_2023-10-08_15-44-22.jpg')
    }
  }
}

</script>

<style scoped>
.clothes_set {
  /* Add your styles here */
  max-width: 100%;
  border: 1px solid #ddd;
  padding: 0.5rem;
  @screen md{
    padding: 1rem;
  }
}

.clothes_set * {
  max-width: 100%;
}

</style>