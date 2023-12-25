<template>
  <site-header></site-header>
  <div style="display: flex"><clothes-set></clothes-set><clothes-set></clothes-set></div>
  <designer-info></designer-info>
  <site-footer></site-footer>
</template>

<script>

import ClothesSet from "@/components/ClothesSet";
import DesignerInfo from "@/components/DesignerInfo";
import SiteFooter from "@/components/SiteFooter";
import SiteHeader from "@/components/SiteHeader";
export default {
  name: 'App',
  components: {SiteHeader, SiteFooter, DesignerInfo, ClothesSet},
}
</script>

<style>

</style>
