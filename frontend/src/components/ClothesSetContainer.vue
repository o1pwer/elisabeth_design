<template>
  <div class="clothes-set-container">
    <ClothesSet v-for="(item, index) in items" :key="index" :style="itemStyle">
      <img :src="item" alt="Clothes set image">
    </ClothesSet>
  </div>
</template>

<script>
import ClothesSet from './ClothesSet.vue';

export default {
  components: {
    ClothesSet
  },
  props: {
    items: {
      type: Array, default:
          () => [require('../assets/media/photo_2023-10-01_20-41-14.jpg'), require('../assets/media/photo_2023-10-08_15-44-22.jpg'),]
    },
  },
  data() {
    return {
      // Define the column gap here so it can be used in the computed property
      columnGap: 10,
    }
  },
  computed: {
    itemStyle() {
      const itemCount = this.items.length;
      // Adjust the width calculation to account for the column gap
      const baseWidth = itemCount <= 3 ? 100 / Math.min(itemCount, 3) : 33.33;
      const gapTotal = this.columnGap * (Math.min(itemCount, 3) - 1);
      const width = itemCount <= 3 ? `calc(${baseWidth}% - ${gapTotal}px)` : `calc(33.33% - ${this.columnGap}px)`;
      return {
        flex: `0 1 ${width}`
      };
    }
  }
}
</script>


<style scoped>
.clothes-set-container {
  display: flex;
  flex-wrap: wrap;
  padding: 1.5rem;
  column-gap: 0.5rem;
  justify-content: space-between;
}
</style>
