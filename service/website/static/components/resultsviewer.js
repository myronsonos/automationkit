

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
    template: `
        <b-card>
            <b-card-title>
                <b-container>
                    <b-row>
                        <b-col>{{ test_result.title }}</b-col>
                        <b-col cols=1>Start:</b-col>
                        <b-col cols=3>{{ test_result.start }}</b-col>
                        <b-col cols=1>Stop:</b-col>
                        <b-col cols=3>{{ test_result.stop }}</b-col>
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

