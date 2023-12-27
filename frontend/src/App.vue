<template>
  <SiteHeader></SiteHeader>
  <router-view></router-view>
  <SiteFooter></SiteFooter>
</template>

<script>

import SiteFooter from "@/components/SiteFooter";
import SiteHeader from "@/components/SiteHeader";

export default {
  name: 'App',
  components: {SiteHeader, SiteFooter},
  methods: {
  },
  data() {
  }
}
</script>

<style>
@import "normalize.css";

@tailwind base;
@tailwind components;
@tailwind utilities;

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
