
Vue.component('device-viewer', {
    // The todo-item component now accepts a
    // "prop", which is like a custom attribute.
    // This prop is called todo.
    props: ['title', 'list_identifier', 'device_list'],
    template: `
        <b-card>
            <b-card-title>{{title}}</b-card-title>
            <b-row>
                <b-col sm="4" style="background: lightyellow;">
                    <devices-list v-bind:list_identifier="list_identifier" v-bind:device_list="device_list"></devices-list>
                </b-col>
                <b-col xl="8" style="background: pink;">
                </b-col>
            </b-row>
        </b-card>
        `
});

Vue.component('devices-list', {
    // The todo-item component now accepts a
    // "prop", which is like a custom attribute.
    // This prop is called todo.
    props: ['list_identifier', 'device_list'],
    template: `
        <b-list-group v-bind:id="list_identifier">
            <device-card v-for="device in device_list" v-bind:list_identifier="list_identifier" v-bind:device="device" v-bind:key="device.MACAddress" ></device-card>
        </b-list-group>
        `
});

Vue.component('device-card', {
    // The todo-item component now accepts a
    // "prop", which is like a custom attribute.
    // This prop is called todo.
    data: {
        isActive: false
    },
    props: ['list_identifier', 'device'],
    methods: {
        selectListItem(evt) {
            var owningList = document.getElementById(this.list_identifier);

            var list_items = owningList.getElementsByClassName("list-group-item");
            for (var idx = 0; idx < list_items.length; idx++) {
                var item = list_items[idx];
                item.classList.remove("active");
            }

            evt.currentTarget.classList.add("active");
        }
    },
    template: `
        <b-list-group-item v-on:click="selectListItem" >
            <b-card>
                <b-row no-gutters>
                    <b-col style="flex-grow: 4;" >
                        <b-card-img v-bind:src="device.cachedIcon" v-bind:img-alt="device.modelNumber" ></b-card-img>
                    </b-col>
                    <b-col style="flex-grow: 20;" align-self="center">
                        <b-card-title class="align-bottom">{{device.modelName}} - {{device.modelNumber}}</b-card-title>
                    </b-col>
                </b-row>
                <b-row no-gutters>
                    <b-container>
                        <b-row>
                            <b-col class="text-right">Household:</b-col><b-col cols='9' class="text-left">{{device.household}}</b-col>
                        </b-row>
                        <b-row>
                            <b-col class="text-right">MAC:</b-col><b-col cols='9' class="text-left">{{device.MACAddress}}</b-col>
                        </b-row>
                        <b-row>
                            <b-col class="text-right">IP:</b-col><b-col cols='9' class="text-left">{{device.IPAddress}}</b-col>
                        </b-row>
                        <b-row>
                            <b-col class="text-right">Version:</b-col><b-col cols='9' class="text-left">{{device.softwareVersion}}</b-col>
                        </b-row>
                    <b-container>
                </b-row>
            </b-card>
        </b-list-group-item>
        `
});

