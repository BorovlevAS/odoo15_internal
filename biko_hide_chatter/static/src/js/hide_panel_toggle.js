odoo.define('hide_panel_toggle.HPanel',function (require) {
"use strict";

	const utils = require('web.utils');
    var Pager = require('web.Pager');
    utils.patch(Pager.prototype, "BIKO.hide.panel", {

        mounted() {
            if ($('body').attr("class").includes('_chatter_position_sided') && $('.o_FormRenderer_chatterContainer').length) {
                $('.o_pager_hide').show();
            } else {
                $('.o_pager_hide').hide();
            }
        },

        _onHideShow: function () {

            let $but = $('.o_pager_hide');
            let $chatter = $('.o_FormRenderer_chatterContainer');

            if ((!$but.length) || (!$chatter.length)) return;

			if ($chatter.hasClass('o_hidden')) {

				$chatter.removeClass('o_hidden');
				$but.removeClass('fa-step-backward').addClass('fa-step-forward');
				$but.attr({
				    'title': 'Hide Chatter',
				    'aria-label': 'Hide'
				});

			} else {

				$chatter.addClass('o_hidden');
				$but.removeClass('fa-step-forward').addClass('fa-step-backward');
				$but.attr({
				    'title': 'Show Chatter',
				    'aria-label': 'Show'
				});
			}

        },
    });

});
