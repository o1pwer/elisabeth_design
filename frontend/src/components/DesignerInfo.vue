<template>
  <div class="designer-info">
    <img :src="designer.photo" alt="Designer's Photo"/>
    <div>
      <h2>{{ designer.name }}</h2>
      <p>{{ designer.biography }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DesignerInfo',
  props: {
    designer: {
      type: Object,
      default: () => {
        return {
          name: 'Elizabeth Cold',
          photo: require('../../../backend/storage/media/photo.png'),
          biography: 'Test'
        }
      }
    }
  }
}
</script>

<style scoped>
.designer-info {
  /* Add your styles here */
  display: flex;
  align-items: center;
  padding: 20px;
  z-index: 1;
}

.designer-info img {
  /* Add your styles for the image here */
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin-right: 20px;
}
</style>
