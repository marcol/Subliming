/*global define*/

define(function () {

    'use strict';

    // Topics
    var topics = {};

    /**
     * Subscribe topic with a callback
     * @param  {String}   topic topic name
     * @param  {Function} fn    callback function
     * @return {Object}         context
     */
    function subscribe(topic, fn) {

        /*jshint validthis: true*/

        if (!topics[topic]) {
            topics[topic] = [];
        }

        topics[topic].push({context: this, callback: fn});

        return this;
    }

    /**
     * Publish a topic
     * @param  {String} topic   topic name
     * @return {Object|Boolean}  context or false
     */
    function publish(topic) {

        /*jshint validthis: true*/

        var i, li, cur;

        if (!topics[topic]) {
            return false;
        }

        for (i = 0, li = topics[topic].length; i < li; i++) {
            cur = topics[topic][i];
            cur.callback.apply(cur.context,  Array.prototype.slice.call(arguments, 1));
        }

        return this;
    }

    // expose
    return {
        publish: publish,
        subscribe: subscribe
    };

});
