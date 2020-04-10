<template>
    <b-card img-src="device.icon" img-alt="device.modelNumber" img-left class="mb-3">
        <b-card-title>{{device.modelName}} - {{device.modelNumber}}</b-card-title>
        <div class="flex-column">
            <div class="d-flex"><div class="h-3">Household:</div><div class="p-2">{{device.household}}</div></div>
            <div class="d-flex"><div class="h-3">MAC:</div><div class="p-2">{{device.MACAddress}}</div></div>
            <div class="d-flex"><div class="h-3">IP:</div><div class="p-2">{{device.IPAddress}}</div></div>
            <div class="d-flex"><div class="h-3">Version:</div><div class="p-2">{{device.softwareVersion}}</div></div>
        </div>
    </b-card>
</template>

<script>
module.exports = {
    props: ['device']
}
</script>

<style scoped>

</style>