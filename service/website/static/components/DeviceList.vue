<template>
    <b-list-group>
        <device-card v-for="device in device_list" :device="device" ></device-card>
    </b-list-group>
</template>

<script>
module.exports = {
    props: ['device_list'],
    components: {
        'device-card': window.httpVueLoader('/static/components/DeviceCard.vue')
    }
}
</script>

<style scoped>

</style>