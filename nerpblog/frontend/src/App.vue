<template>
    <top-panel></top-panel>
    <!-- <nav-bar></nav-bar> -->
    <router-view></router-view>
</template>


<script setup>
import TopPanel from '@/components/TopPanel.vue'
import { RouterView } from 'vue-router'





</script>


<style>
@import url('https://fonts.googleapis.com/css2?family=Mulish:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;0,1000;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900;1,1000&display=swap');

body, #app {
    margin: 0px;
    display: flex;
    width: 100%;
    height: 100%;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    background: #121212;
    box-sizing: border-box;
}
</style>