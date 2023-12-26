<template>
  <SiteContainer>
    <SiteHeader></SiteHeader>
    <ClothesSetContainer>
      <ClothesSet></ClothesSet>
      <ClothesSet></ClothesSet>
    </ClothesSetContainer>
    <DesignerInfo></DesignerInfo>
    <SiteFooter></SiteFooter>
  </SiteContainer>
</template>

<script>

import ClothesSet from "@/components/ClothesSet";
import DesignerInfo from "@/components/DesignerInfo";
import SiteFooter from "@/components/SiteFooter";
import SiteHeader from "@/components/SiteHeader";
import SiteContainer from "@/components/SiteContainer";
import ClothesSetContainer from "@/components/ClothesSetContainer";

export default {
  name: 'App',
  components: {ClothesSetContainer, SiteContainer, SiteHeader, SiteFooter, DesignerInfo, ClothesSet},
}
</script>

<style>
@import "normalize.css";
</style>
