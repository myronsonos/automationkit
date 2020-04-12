

Vue.component('device-viewer', {
    // The todo-item component now accepts a
    // "prop", which is like a custom attribute.
    // This prop is called todo.
    props: {
        title: {
            type: String,
            default: "Some Device Viewer"
        }, 
        list_identifier: {
            type: String,
            default: "not-set"
        },
        detail_identifier: {
            type: String,
            default: "not-set"
        },
        device_list: {
            default: function() {
                return {}
            }
        }
    },
    template: `
        <b-card >
            <b-card-title>{{title}}</b-card-title>
            <b-row>
                <b-col sm="4" style="background: lightyellow;">
                    <devices-list v-bind:list_identifier="list_identifier"
                                  v-bind:detail_identifier="detail_identifier"
                                  v-bind:device_list="device_list"></devices-list>
                </b-col>
                <b-col xl="8" style="background: pink;">
                    <dev-detail-view v-bind:detail_identifier="detail_identifier" ></dev-detail-view>
                </b-col>
            </b-row>
        </b-card>
        ` // End of Template
});

Vue.component('devices-list', {
    // The todo-item component now accepts a
    // "prop", which is like a custom attribute.
    // This prop is called todo.
    props: {
        list_identifier: {
            type: String,
            default: "not-set"
        },
        detail_identifier: {
            type: String,
            default: "not-set"
        },
        device_list: {
            default: function() {
                return {}
            }
        }
    },
    template: `
        <b-list-group v-bind:id="list_identifier">
            <device-card v-for="device in device_list" v-bind:device="device"
                         v-bind:list_identifier="list_identifier"
                         v-bind:detail_identifier="detail_identifier"
                         v-bind:key="device.MACAddress" ></device-card>
        </b-list-group>
        ` // End of Template
});

Vue.component('device-card', {
    // The todo-item component now accepts a
    // "prop", which is like a custom attribute.
    // This prop is called todo.
    props: {
        list_identifier: {
            type: String,
            default: "not-set"
        },
        detail_identifier: {
            type: String,
            default: "not-set"
        },
        device: {
            default: function() {
                return {}
            }
        }
    },
    methods: {
        selectListItem(evt) {
            var owningList = document.getElementById(this.list_identifier);

            var list_items = owningList.getElementsByClassName("list-group-item");
            for (var idx = 0; idx < list_items.length; idx++) {
                var item = list_items[idx];
                item.classList.remove("active");
            }

            evt.currentTarget.classList.add("active");

            var detailView = document.getElementById(this.detail_identifier);
            var vinst = detailView.__vue__;
            var mac = this.device.MACAddress;
            vinst.setDeviceDetail(mac);
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
                    </b-container>
                </b-row>
            </b-card>
        </b-list-group-item>
        ` // End of Template
});


Vue.component('dev-detail-view', {
    // The todo-item component now accepts a
    // "prop", which is like a custom attribute.
    // This prop is called todo.
    data : function() {
        var dobj  = {
            device: {},
            mac: "not-set"
        }
        return dobj;
    },
    props: {
        detail_identifier: {
            type: String,
            default: "not-set"
        }
    },
    computed: {
        propertyList: function() {
            var entries = [];

            var sortedKeys = Object.keys(this.device).sort(function (a, b) {
                return a.toLowerCase().localeCompare(b.toLowerCase());
            });

            sortedKeys = sortedKeys.filter(val => val != "serviceList");
            sortedKeys = sortedKeys.filter(val => val != "serviceDescriptionList")
            sortedKeys = sortedKeys.filter(val => val != "iconList")
            sortedKeys = sortedKeys.filter(val => val != "deviceList")

            var vidx = 0;
            var vkeyCount = sortedKeys.length;
            while(vidx < vkeyCount) {
                var vkey = sortedKeys[vidx];
                var vval = this.device[vkey];
                entries.push([vkey, vval]);
                vidx += 1;
            }

            return entries;
        },
        serviceDescriptionList: function () {
            var sdlist = [];
            
            if ("serviceDescriptionList" in this.device) {
                var serviceTable = {};
                var serviceList = this.device["serviceDescriptionList"];

                for (sidx in serviceList) {
                    var svcObj = serviceList[sidx];
                    serviceTable[svcObj["serviceType"]] = svcObj;
                }

                var sortedKeys = Object.keys(serviceTable).sort(function (a, b) {
                    return a.toLowerCase().localeCompare(b.toLowerCase());
                });

                var vidx = 0;
                var vkeyCount = sortedKeys.length;
                while(vidx < vkeyCount) {
                    var vkey = sortedKeys[vidx];
                    var vval = serviceTable[vkey];
                    sdlist.push([vkey, vval]);
                    vidx += 1;
                }
            }

            return sdlist;
        }
    },
    methods: {
        setDeviceDetail(mac) {
            this.mac = mac;

            // We iterate on this.device so we need to update mac first
            // so it will be set before device so the render will work
            // correctly.
            var qurl = "/api/1/devices/" + encodeURIComponent(mac);
            axios.get(qurl).then(
                (response) => {
                    device = response.data.device;
                    this.device = device;
                }
            );
        }
    },
    template: `
        <b-card title="Device Detail" v-bind:id="detail_identifier">
            <b-card-body>
                <b-container>
                    <details>
                        <summary><span class='h4'>Properties</span></summary>
                        <b-container>
                            <dev-detail-node-select v-for="[pkey, pval], pindex in propertyList" 
                                v-bind:detail_identifier="detail_identifier"
                                v-bind:parent_identifier="detail_identifier"
                                v-bind:self_identifier='detail_identifier + "-" + pkey'
                                v-bind:mac='mac'
                                v-bind:node_name="pkey"
                                v-bind:node_value="pval"
                                v-bind:key="pindex" >
                            </dev-detail-node-select>
                        </b-container>
                    </details>
                    <details>
                        <summary><span class='h4'>Services</span></summary>
                        <b-container>
                            <dev-detail-node-svc v-for="[pkey, pval], pindex in serviceDescriptionList" 
                                v-bind:detail_identifier='detail_identifier'
                                v-bind:parent_identifier='detail_identifier'
                                v-bind:self_identifier='detail_identifier + "-" + pkey'
                                v-bind:mac='mac'
                                v-bind:node_name='pkey'
                                v-bind:node_value='pval'
                                v-bind:key="pindex">
                            </dev-detail-node-svc>
                        </b-container>
                    </details>
                </b-container>
            </b-card-body>
        </b-card>
        ` // End of Template
});


Vue.component('dev-detail-node-select', {
    // The todo-item component now accepts a
    // "prop", which is like a custom attribute.
    // This prop is called todo.
    props: {
        detail_identifier: {
            type: String,
            default: "not-set"
        },
        parent_identifier: {
            type: String,
            default: "not-set"
        },
        self_identifier: {
            type: String,
            default: "not-set"
        },
        mac: {
            type: String,
            default: "not-set",
        },
        node_name: {
            type: String,
            default: "not_set"
        },
        node_value: {
            default: function() {
                return {}
            }
        }
    },
    template: `
        <dev-detail-node-kv v-if='node_value == undefined'
                            v-bind:detail_identifier="detail_identifier"
                            v-bind:parent_identifier="parent_identifier"
                            v-bind:self_identifier="self_identifier"
                            v-bind:mac='mac'
                            v-bind:node_name='node_name'
                            v-bind:node_value="'undefined'">
        </dev-detail-node-kv>
        <dev-detail-node-kv v-else-if='node_value == null'
                            v-bind:detail_identifier="detail_identifier"
                            v-bind:parent_identifier="parent_identifier"
                            v-bind:self_identifier="self_identifier"
                            v-bind:mac='mac'
                            v-bind:node_name='node_name'
                            v-bind:node_value="'null'">
        </dev-detail-node-kv>
        <dev-detail-node-kv v-else-if='Object.keys(node_value).length == 0'
                            v-bind:detail_identifier="detail_identifier"
                            v-bind:parent_identifier="parent_identifier"
                            v-bind:self_identifier="self_identifier"
                            v-bind:mac='mac'
                            v-bind:node_name='node_name'
                            v-bind:node_value='node_value'>
        </dev-detail-node-kv>
        <dev-detail-node-unknown v-else
                            v-bind:detail_identifier='detail_identifier'
                            v-bind:parent_identifier='parent_identifier'
                            v-bind:self_identifier='self_identifier'
                            v-bind:mac='mac'
                            v-bind:node_name='node_name'
                            v-bind:node_value='node_value'>
        </dev-detail-node-unknown>
        ` // End of Template
});


Vue.component('dev-detail-node-ignore', {
    // The todo-item component now accepts a
    // "prop", which is like a custom attribute.
    // This prop is called todo.
    props: {
        detail_identifier: {
            type: String,
            default: "not-set"
        },
        parent_identifier: {
            type: String,
            default: "not-set"
        },
        self_identifier: {
            type: String,
            default: "not-set"
        },
        mac: {
            type: String,
            default: "not-set",
        },
        node_name: {
            type: String,
            default: "not_set"
        },
        node_value: {
            default: function() {
                return {}
            }
        }
    },
    template: `
        <!-- Skipping - {{ node_name }} -->
        ` // End of Template
});

Vue.component('dev-detail-node-kv', {
    // The todo-item component now accepts a
    // "prop", which is like a custom attribute.
    // This prop is called todo.
    props: {
        detail_identifier: {
            type: String,
            default: "not-set"
        },
        parent_identifier: {
            type: String,
            default: "not-set"
        },
        self_identifier: {
            type: String,
            default: "not-set"
        },
        mac: {
            type: String,
            default: "not-set",
        },
        node_name: {
            type: String,
            default: "not_set"
        },
        node_value: {
            default: function() {
                return {}
            }
        }
    },
    template: `
        <b-row v-bind:id="self_identifier" >
            <b-col cols=3 class='text-right border-bottom border-dark' style="background: lightgray;">{{ node_name }}:</b-col>
            <b-col class='border-bottom border-dark' sytle="padding-left: 10px;">{{ node_value }}</b-col>
        </b-row>
        ` // End of Template
});

Vue.component('dev-detail-node-icon-list', {
    // The todo-item component now accepts a
    // "prop", which is like a custom attribute.
    // This prop is called todo.
    props: {
        detail_identifier: {
            type: String,
            default: "not-set"
        },
        parent_identifier: {
            type: String,
            default: "not-set"
        },
        self_identifier: {
            type: String,
            default: "not-set"
        },
        mac: {
            type: String,
            default: "not-set",
        },
        node_name: {
            type: String,
            default: "not_set"
        },
        node_value: {
            type: String,
            default: "(not set)"
        }
    },
    template: `
        
        ` // End of Template
});

Vue.component('dev-detail-node-svc', {
    // The todo-item component now accepts a
    // "prop", which is like a custom attribute.
    // This prop is called todo.
    props: {
        detail_identifier: {
            type: String,
            default: "not-set"
        },
        parent_identifier: {
            type: String,
            default: "not-set"
        },
        self_identifier: {
            type: String,
            default: "not-set"
        },
        mac: {
            type: String,
            default: "not-set",
        },
        node_name: {
            type: String,
            default: "not_set"
        },
        node_value: {
            default: function() {
                return {}
            }
        }
    },
    template: `
        <details>
            <summary><span class='h5'>{{ node_value.serviceType }}</span></summary>
            <b-container>
                <b-row>
                    <b-col cols=3 class='text-right border-bottom border-dark' style='background: lightgray;'>
                        <span class='h5'>specVersion:</span>
                    </b-col>
                    <b-col class='border-bottom border-dark' sytle='padding-left: 10px;'>{{ node_value.specVersion.major }}, {{ node_value.specVersion.minor }}</b-col>
                </b-row>
                <details v-if='Object.keys(node_value.actionsTable).length > 0'>
                    <summary><span class='h5'>Actions</span></summary>
                    <b-container>
                        <b-row v-for='vval, vkey, vidx in node_value.actionsTable'>
                            <b-col cols=3 class='text-right border-bottom border-dark' style='background: lightgray;'>
                                <span class='h5'>{{ vkey }}:</span>
                            </b-col>
                            <b-col class='border-bottom border-dark' sytle='padding-left: 10px;'>{{ vval }}</b-col>
                        </b-row>
                    </b-container>
                </details>
                <details v-if='Object.keys(node_value.eventsTable).length > 0'>
                    <summary><span class='h5'>Events</span></summary>
                    <b-container>
                        <b-row v-for='vval, vkey, vidx in node_value.eventsTable'>
                            <b-col cols=3 class='text-right border-bottom border-dark' style='background: lightgray;'>
                                <span class='h5'>{{ vkey }}:</span>
                            </b-col>
                            <b-col class='border-bottom border-dark' sytle='padding-left: 10px;'>{{ vval }}</b-col>
                        </b-row>
                    </b-container>
                </details>
                <details v-if='Object.keys(node_value.typesTable).length > 0'>
                    <summary><span class='h5'>Types</span></summary>
                    <b-container>
                        <b-row v-for='vval, vkey, vidx in node_value.typesTable'>
                            <b-col cols=3 class='text-right border-bottom border-dark' style='background: lightgray;'>
                                <span class='h5'>{{ vkey }}:</span>
                            </b-col>
                            <b-col class='border-bottom border-dark' sytle='padding-left: 10px;'>{{ vval }}</b-col>
                        </b-row>
                    </b-container>
                </details>
                <details v-if='Object.keys(node_value.variablesTable).length > 0'>
                    <summary><span class='h5'>Variables</span></summary>
                    <b-container>
                        <b-row v-for='vval, vkey, vidx in node_value.variablesTable'>
                            <b-col cols=3 class='text-right border-bottom border-dark' style='background: lightgray;'>
                                <span class='h5'>{{ vkey }}:</span>
                            </b-col>
                            <b-col class='border-bottom border-dark' sytle='padding-left: 10px;'>{{ vval }}</b-col>
                        </b-row>
                    </b-container>
                </details>
            </b-container>
        </details>
        ` // End of Template

});

Vue.component('dev-detail-node-unknown', {
    // The todo-item component now accepts a
    // "prop", which is like a custom attribute.
    // This prop is called todo.
    props: {
        detail_identifier: {
            type: String,
            default: "not-set"
        },
        parent_identifier: {
            type: String,
            default: "not-set"
        },
        self_identifier: {
            type: String,
            default: "not-set"
        },
        mac: {
            type: String,
            default: "not-set",
        },
        node_name: {
            type: String,
            default: "not_set"
        },
        node_value: {
            default: function() {
                return {}
            }
        }
    },
    template: `
        <b-row v-bind:id="self_identifier" >
            <b-col cols=3 class='text-right border-bottom border-dark' style="background: lightgray;">
            <span class='h5'>{{ node_name }}:</span>
            </b-col>
            <b-col class='border-bottom border-dark' sytle="padding-left: 10px;">{{ node_value }}</b-col>
        </b-row>
        ` // End of Template
});
