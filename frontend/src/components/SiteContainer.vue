<template>
  <div class="site-container">
    <ClothesSetContainer>
    </ClothesSetContainer>
    <DesignerInfo></DesignerInfo>
  </div>
</template>

<script>
import ClothesSetContainer from "@/components/ClothesSetContainer";
import DesignerInfo from "@/components/DesignerInfo";
export default {
  name: "SiteContainer",
  components: {ClothesSetContainer, DesignerInfo}
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