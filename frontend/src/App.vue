<template>
  <SiteContainer>
    <SiteHeader></SiteHeader>
    <ClothesSetContainer :items="getClothesSets()">
    </ClothesSetContainer>
    <DesignerInfo></DesignerInfo>
  </SiteContainer>
  <SiteFooter></SiteFooter>
</template>

<script>

import DesignerInfo from "@/components/DesignerInfo";
import SiteFooter from "@/components/SiteFooter";
import SiteHeader from "@/components/SiteHeader";
import SiteContainer from "@/components/SiteContainer";
import ClothesSetContainer from "@/components/ClothesSetContainer";

export default {
  name: 'App',
  components: {ClothesSetContainer, SiteContainer, SiteHeader, SiteFooter, DesignerInfo},
  methods: {
    getClothesSets() {
      return [require('./assets/media/photo_2023-10-01_20-41-14.jpg'), require('./assets/media/photo_2023-10-08_15-44-22.jpg'),]
    },
  }
}
</script>

<style>
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';
@import "normalize.css";

* {
  box-sizing: border-box;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.clothes_set * {
  max-width: 100%;
}
</style>
