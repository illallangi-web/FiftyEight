(function ($) {

    var count = 1,
        stylesheets = {},
        gistUrlRegex = new RegExp('^(https?://)?gist.github.com/([0-9]+)(#file_(.*))?$');

    $.gist = function (id, file, placeholder) {
        if (!id || id === $) {
            // no arguments, replace all anchors in document
            $(document).gist();
        } else {
            placeholder = placeholder || ['gist', id, count++].join('-');
            $('<div />', { 'id': placeholder }).appendTo('body').gist(id, file);
        }
    };

    $.gist.url = function (id, file) {
        var $this;
        var https = false;
        if (!id && ($this = $(this)).is('a')) {
            // no id specified, get from anchor href
            var match = gistUrlRegex.exec($this.attr('href'));
            if (match) {
                https = match[1] == 'https://';
                id = match[2];
                file = match[4] || file;
            }
        } else if (typeof id == 'object') {
            file = typeof id.file == 'function' ? id.file.apply(this) : id.file;
            id = typeof id.id == 'function' ? id.id.apply(this) : id.id;
        }
        if (!id) {
            return null;
        }
        var url = (https ? 'https' : 'http') + '://gist.github.com/' + id + '.json?';
        if (file) {
            url += 'file=' + file + '&';
        }
        url += 'callback=?';
        return url;
    };

    $.fn.gist = function (id, file) {


        if (!id && !this.is('a')) {
            // container and no parameters, call on contained anchors
            return this.find('a').gist();
        }

        for (var i = 0, l = this.length; i < l; i++) {

            var self = this[i];

            var url = $.gist.url.apply(self, arguments);
            if (url) {
                $.ajax(url, {
                    dataType: 'json',
                    context: self,
                    success: function (json) {
                        // embed gist
                        $(json.div).replaceAll(this).trigger('gistloaded', json);

                        // add stylesheet
                        if (json.stylesheet && !stylesheets[json.stylesheet]) {
                            if (!$(document.head).find('link[rel=stylesheet]').filter(function () { return this.href == json.stylesheet; }).length) {
                                $(document.head).append('<link rel="stylesheet" href="' + json.stylesheet + '"/>');
                            }
                            stylesheets[json.stylesheet] = json.stylesheet;
                        }
                    }
                });
            }
        }

        return this;
    };

})(jQuery);
