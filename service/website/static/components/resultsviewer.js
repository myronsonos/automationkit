

Vue.component('test-result-viewer', {
    // The todo-item component now accepts a
    // "prop", which is like a custom attribute.
    // This prop is called todo.
    props: {
        title: {
            type: String,
            default: "not set"
        },
        test_result_list: {
            default: function() {
                return {}
            }
        }
    },
    template: `
        <b-container style='margin-left: 0px; margin-right: 0px; max-width: 100%;'>
            <b-row style='width: 100%;'>
                <b-col></b-col>
                <b-col cols=10><div class='h2'>{{ title }}</div></b-col>
                <b-col></b-col>
            </b-row>
            <b-row style='width: 100%;'>
                <b-col></b-col>
                <b-col cols=10>
                    <test-result-item-card v-for='pval, pidx in test_result_list'
                        v-bind:test_result='pval'>
                    </test-result-item-card>
                </b-col>
                <b-col></b-col>
            </b-row>
        </b-container>
        ` // End of Template
});

Vue.component('test-result-item-card', {
    // The todo-item component now accepts a
    // "prop", which is like a custom attribute.
    // This prop is called todo.
    props: {
        test_result: {
            default: function() {
                return {}
            }
        }
    },
    computed: {
        summary_html_report: function () {
            var report_url = window.location.protocol + "//" + window.location.host + this.test_result.htmlreport;
            return report_url;
        }
    },
    template: `
        <b-card>
            <b-card-title>
                <b-container>
                    <b-row>
                        <b-col cols=4>{{ test_result.title }}</b-col>
                        <b-col cols=1>Start:</b-col>
                        <b-col cols=3>{{ test_result.start.substring(0, test_result.start.length - 7 ) }}</b-col>
                        <b-col cols=1>Stop:</b-col>
                        <b-col cols=3>{{ test_result.stop.substring(0, test_result.stop.length - 7 ) }}</b-col>
                    </b-row>
                    <b-row>
                        <b-col cols=2>Branch:</b-col>
                        <b-col cols=2>{{ test_result.branch }}</b-col>
                        <b-col cols=2>Build:</b-col>
                        <b-col cols=2>{{ test_result.build }}</b-col>
                        <b-col cols=2>Flavor:</b-col>
                        <b-col cols=2>{{ test_result.flavor }}</b-col>
                    </b-row>
                    <b-row>
                        <b-col>Errors:</b-col>
                        <b-col>{{ test_result.detail.errors }}</b-col>
                        <b-col>Failed:</b-col>
                        <b-col>{{ test_result.detail.failed }}</b-col>
                        <b-col>Skipped:</b-col>
                        <b-col>{{ test_result.detail.skipped }}</b-col>
                        <b-col>Passed:</b-col>
                        <b-col>{{ test_result.detail.passed }}</b-col>
                        <b-col>Total:</b-col>
                        <b-col>{{ test_result.detail.total }}</b-col>
                        <b-col cols=1>
                            <b-badge v-if='test_result.result.toLowerCase() == "error"' variant="danger">{{ test_result.result }}</b-badge>
                            <b-badge v-else-if='test_result.result.toLowerCase() == "failed"' variant="danger">{{ test_result.result }}</b-badge>
                            <b-badge v-else-if='test_result.result.toLowerCase() == "passed"' variant="success">{{ test_result.result }}</b-badge>
                            <b-badge v-else-if='test_result.result.toLowerCase() == "skipped"' variant="secondary">{{ test_result.result }}</b-badge>
                            <b-badge v-else >{{ test_result.result }}</b-badge>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col>
                            <b-link v-bind:href="summary_html_report">{{ summary_html_report }}</b-link>
                        </b-col>
                    </b-row>
                </b-container>
            </b-card-title>
            <b-container>
            </b-container>
        </b-card>
        ` // End of Template
});

/*
    {
      "title": "Automation Test Run",
      "runid": "1d30b3b5-8774-42ff-ad88-86e4571b5f08",
      "branch": null,
      "build": null,
      "flavor": null,
      "start": "2020-03-20 23:18:48.335152",
      "stop": "2020-03-20 23:18:48.362281",
      "result": "FAILED",
      "landscape": null,
      "detail": {
        "errors": 0,
        "failed": 1,
        "skipped": 0,
        "passed": 3,
        "total": 4
      },
      "htmlreport": "/home/myron/akit/results/testresults/2020-03-20T23:18:48.335152/testsummary.html"
    },
*/

