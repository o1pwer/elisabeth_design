<template>
  <div class="site-container">
    <ClothesSetContainer :items="items">
    </ClothesSetContainer>
    <DesignerInfo></DesignerInfo>
  </div>
</template>

<script>
import ClothesSetContainer from "@/components/ClothesSetContainer";
import DesignerInfo from "@/components/DesignerInfo";

export default {
  name: "SiteContainer",
  components: {ClothesSetContainer, DesignerInfo},
  data() {
    return {
      items: [],
    }
  },
  created() {
    fetch("/api/v1/clothes/list/clothes_sets")
        .then(response => response.json())
        .then(data => (this.items = data.clothes_sets));
  }
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