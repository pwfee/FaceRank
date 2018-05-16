/*
 * jQuery File Upload Plugin JS Example
 * https://github.com/blueimp/jQuery-File-Upload
 *
 * Copyright 2010, Sebastian Tschan
 * https://blueimp.net
 *
 * Licensed under the MIT license:
 * https://opensource.org/licenses/MIT
 */

/* global $, window */

$(function () {
    'use strict';
    // Initialize the jQuery File Upload widget:
    $('#fileupload').fileupload({
        // Uncomment the following to send cross-domain cookies:
        //xhrFields: {withCredentials: true},
        url: '/api/upload_image',
    }).bind('fileuploaddone', function (e, data) {
        var image_id =  data.result["files"][0]["image_id"];
        setTimeout(function () {
            $.ajax({
                url: '/api/image_status?id=' + image_id,
                type: "get",
                dataType: "json",
                success: function (data) {
                    console.log(data.score);
                },
            })
        }, 2000);
    });
});
