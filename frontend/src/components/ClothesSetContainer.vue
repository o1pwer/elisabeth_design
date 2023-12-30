<template>
  <div class="clothes-set-container">
    <ClothesSet v-for="(item, index) in items" :key="index" :style="itemStyle">
      <img v-if="item.images.length > 0" :src="item.images[0].link" alt="Clothes set image">
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
    items: Array,
  },
  methods: {
    addToCounter() {
      // Adds 1 to itemStyle calls counter
      this.itemStyleCallCounter += 1;
    },
    clearCounter() {
      // Clears counter
      this.itemStyleCallCounter = 0;
    },

  },
  data() {
    return {
      // Define the column gap here so it can be used in the computed property (in rem)
      columnGap: 0.5,
      itemStyleCallCounter: 0,
    }
  },
  computed: {
    itemStyle() {
      let itemCount = this.items.length;
      if (this.itemStyleCallCounter === 3) {
        itemCount = 0;
        this.clearCounter();
      }
      this.addToCounter();
      // Adjust the width calculation to account for the column gap
      const singleImageWidth = 100/ Number((Math.min(itemCount, 3)).toFixed(2));
      const baseWidth = 100 / singleImageWidth;
      const gapTotal = this.columnGap * (Math.min(itemCount, 3) - 1);
      const width = itemCount <= 3 ? `calc(${baseWidth}% - ${gapTotal}rem)` : `calc(${singleImageWidth}% - ${this.columnGap}rem)`;
      return {
        flex: `1 0 ${width}`
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
  row-gap: 0.5rem;
  justify-content: space-between;
}
</style>
