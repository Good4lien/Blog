/**
 * Prestige skin for CKEditor
 * Based on default Moono-Lisa theme.
 * @author Michael Dearman <mickeyuk@live.co.uk>
 * @license Copyright (c) 2003-2017, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or https://ckeditor.com/license
 */
CKEDITOR.skin.name = 'prestige';

// Browser specific hack files
CKEDITOR.skin.ua_editor = 'ie,iequirks,ie8,gecko';
CKEDITOR.skin.ua_dialog = 'ie,iequirks,ie8';

// Chameleon feature (UI Color)
CKEDITOR.skin.chameleon = ( function() {

	var colorBrightness = ( function() {
		function channelBrightness( channel, ratio ) {
			var brighten = ratio < 0 ? (
					0 | channel * ( 1 + ratio )
				) : (
					0 | channel + ( 255 - channel ) * ratio
				);

			return ( '0' + brighten.toString( 16 ) ).slice( -2 );
		}

		return function( hexColor, ratio ) {
			var channels = hexColor.match( /[^#]./g );

			for ( var i = 0 ; i < 3 ; i++ )
				channels[ i ] = channelBrightness( parseInt( channels[ i ], 16 ), ratio );

			return '#' + channels.join( '' );
		};
	} )(),

	// Style templates for various user interface parts:
	// 	* Default editor template.
	// 	* Default panel template.
	templates = {
		editor: new CKEDITOR.template(
			'{id}.cke_chrome [' +
					'border-color:{defaultBorder};' +
				'] ' +
			'{id} .cke_top [ ' +
					'background-color:{defaultBackground};' +
					'border-bottom-color:{defaultBorder};' +
				'] ' +
			'{id} .cke_bottom [' +
					'background-color:{defaultBackground};' +
					'border-top-color:{defaultBorder};' +
				'] ' +
			'{id} .cke_resizer [' +
					'border-right-color:{ckeResizer}' +
				'] ' +

			// Dialogs.
			'{id} .cke_dialog_title [' +
					'background-color:{defaultBackground};' +
					'border-bottom-color:{defaultBorder};' +
				'] ' +
			'{id} .cke_dialog_footer [' +
					'background-color:{defaultBackground};' +
					'outline-color:{defaultBorder};' +
				'] ' +
			'{id} .cke_dialog_tab [' +
					'background-color:{dialogTab};' +
					'border-color:{defaultBorder};' +
				'] ' +
			'{id} .cke_dialog_tab:hover [' +
					'background-color:{lightBackground};' +
				'] ' +
			'{id} .cke_dialog_contents [' +
					'border-top-color:{defaultBorder};' +
				'] ' +
			'{id} .cke_dialog_tab_selected, {id} .cke_dialog_tab_selected:hover [' +
					'background:{dialogTabSelected};' +
					'border-bottom-color:{dialogTabSelectedBorder};' +
				'] ' +
			'{id} .cke_dialog_body [' +
					'background:{dialogBody};' +
					'border-color:{defaultBorder};' +
				'] ' +

			// Toolbars, buttons.
			'{id} a.cke_button_off:hover,' +
			'{id} a.cke_button_off:focus,' +
			'{id} a.cke_button_off:active [' +
					'background-color:{darkBackground};' +
					'border-color:{toolbarElementsBorder};' +
				'] ' +
			'{id} .cke_button_on [' +
					'background-color:{ckeButtonOn};' +
					'border-color:{toolbarElementsBorder};' +
				'] ' +
			'{id} .cke_toolbar_separator,' +
			'{id} .cke_toolgroup a.cke_button:last-child:after,' +
			'{id} .cke_toolgroup a.cke_button.cke_button_disabled:hover:last-child:after [' +
					'background-color: {toolbarElementsBorder};' +
					'border-color: {toolbarElementsBorder};' +
				'] ' +

			// Combo buttons.
			'{id} a.cke_combo_button:hover,' +
			'{id} a.cke_combo_button:focus,' +
			'{id} .cke_combo_on a.cke_combo_button [' +
					'border-color:{toolbarElementsBorder};' +
					'background-color:{darkBackground};' +
				'] ' +
			'{id} .cke_combo:after [' +
					'border-color:{toolbarElementsBorder};' +
				'] ' +

			// Elementspath.
			'{id} .cke_path_item [' +
					'color:{elementsPathColor};' +
				'] ' +
			'{id} a.cke_path_item:hover,' +
			'{id} a.cke_path_item:focus,' +
			'{id} a.cke_path_item:active [' +
					'background-color:{darkBackground};' +
				'] ' +
			'{id}.cke_panel [' +
				'border-color:{defaultBorder};' +
			'] '
		),
		panel: new CKEDITOR.template(
			// Panel drop-downs.
			'.cke_panel_grouptitle [' +
					'background-color:{lightBackground};' +
					'border-color:{defaultBorder};' +
				'] ' +

			// Context menus.
			'.cke_menubutton_icon [' +
					'background-color:{menubuttonIcon};' +
				'] ' +
			'.cke_menubutton:hover,' +
			'.cke_menubutton:focus,' +
			'.cke_menubutton:active [' +
					'background-color:{menubuttonHover};' +
				'] ' +
			'.cke_menubutton:hover .cke_menubutton_icon, ' +
			'.cke_menubutton:focus .cke_menubutton_icon, ' +
			'.cke_menubutton:active .cke_menubutton_icon [' +
					'background-color:{menubuttonIconHover};' +
				'] ' +
			'.cke_menubutton_disabled:hover .cke_menubutton_icon,' +
			'.cke_menubutton_disabled:focus .cke_menubutton_icon,' +
			'.cke_menubutton_disabled:active .cke_menubutton_icon [' +
					'background-color:{menubuttonIcon};' +
				'] ' +
			'.cke_menuseparator [' +
					'background-color:{menubuttonIcon};' +
				'] ' +

			// Color boxes.
			'a:hover.cke_colorbox, ' +
			'a:active.cke_colorbox [' +
					'border-color:{defaultBorder};' +
				'] ' +
			'a:hover.cke_colorauto, ' +
			'a:hover.cke_colormore, ' +
			'a:active.cke_colorauto, ' +
			'a:active.cke_colormore [' +
					'background-color:{ckeColorauto};' +
					'border-color:{defaultBorder};' +
				'] '
		)
	};

	return function( editor, part ) {
		var uiColor = editor.uiColor,
			baseColor = colorBrightness( uiColor, 0.4 ),
			// The following are CSS styles used in templates.
			// Styles are generated according to current editor.uiColor.
			templateStyles = {
				// CKEditor instances have a unique ID, which is used as class name into
				// the outer container of the editor UI (e.g. ".cke_1").
				//
				// The Chameleon feature is available for each CKEditor instance,
				// independently. Because of this, we need to prefix all CSS selectors with
				// the unique class name of the instance.
				id: '.' + editor.id,

				// These styles are used by various UI elements.
				defaultBorder: colorBrightness( baseColor, -0.2 ),
				toolbarElementsBorder: colorBrightness( baseColor, -0.25 ),
				defaultBackground: baseColor,
				lightBackground: colorBrightness( baseColor, 0.8 ),
				darkBackground: colorBrightness( baseColor, -0.15 ),

				// These are for specific UI elements.
				ckeButtonOn: colorBrightness( baseColor, 0.4 ),
				ckeResizer: colorBrightness( baseColor, -0.4 ),
				ckeColorauto: colorBrightness( baseColor, 0.8 ),
				dialogBody: colorBrightness( baseColor, 0.7 ),
				dialogTab: colorBrightness( baseColor, 0.65 ),
				dialogTabSelected: '#FFF',
				dialogTabSelectedBorder: '#FFF',
				elementsPathColor: colorBrightness( baseColor, -0.6 ),
				menubuttonHover: colorBrightness( baseColor, 0.1 ),
				menubuttonIcon: colorBrightness( baseColor, 0.5 ),
				menubuttonIconHover: colorBrightness( baseColor, 0.3 )
			};

		return templates[ part ]
			.output( templateStyles )
			.replace( /\[/g, '{' )				// Replace brackets with braces.
			.replace( /\]/g, '}' );
	};
} )();