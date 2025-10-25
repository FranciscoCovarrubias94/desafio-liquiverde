<template>
  <v-app>
    <v-navigation-drawer app permanent color="green-lighten-5">
      <v-list>
        <v-list-item title="EcoShop MVP" subtitle="v0.1" />
        <v-divider class="my-2" />
        <v-list-item
          link
          title="Escáner"
          prepend-icon="mdi-barcode-scan"
          :to="{ name: 'scanner' }"
        />
        <v-list-item
          link
          title="Optimización"
          prepend-icon="mdi-leaf"
          :to="{ name: 'optimize' }"
        />
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app color="green-lighten-3" title="EcoApp" />

    <v-main>
        <v-container class="pa-6" fluid>
            <router-view />
        </v-container>
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
// Layout principal con sidebar
</script>
