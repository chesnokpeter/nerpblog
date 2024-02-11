<template>
    <div :class="['panel',{'fixed': fixed}]" >nerpblog</div>
</template>

<script>

export default {
    data() {
        return {
            fixed: false
        }
    },
    mounted() {

    }  
}

</script>

<style scoped lang="scss">
    .panel {
        display: flex;
        height: 150px;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 10px;
        /* flex: 1 0 0; */
        align-self: stretch;
        color: #FFF;
        font-family: 'Mulish';
        font-size: 24px;
        font-style: normal;
        font-weight: 700;
        line-height: normal; 
        background-color: #202020;
        // margin-bottom: 30px;

    }

</style>