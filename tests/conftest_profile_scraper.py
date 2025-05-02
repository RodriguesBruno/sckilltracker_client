import pytest


@pytest.fixture
def pilot_with_no_corp_profile():
    return """
    <!DOCTYPE html>
    <html lang="en">
      <head>
    
        <script
        id="TagManager"
        data-cookieconsent="ignore"
        data-app-name="rsi-heap"
        data-app-version="9.177.0"
        data-category="account"
        data-sub-category="account-profile-public"
        src="/tag-manager/script.js"
        type="text/javascript"></script>
            <script
        type="text/javascript"
        id="Cookiebot"
        src="https://consent.cookiebot.com/uc.js"
        data-cbid="a687ee30-df65-45a0-9d22-90de6c1bb964"
        data-blockingmode="auto"
        data-georegions="{'region':'US-06,US-51,AT,BE,BG,HR,CY,CZ,DK,EE,FI,FR,DE,GR,HU,IE,IT,LV,LT,LU,MT,NL,PL,PT,RO,SK,SL,ES,SE','cbid':'a687ee30-df65-45a0-9d22-90de6c1bb964'}"></script>
        <script id="CookieConsent" src="/cookie-consent/script.js?async=false" type="text/javascript"></script>
      <link href="/rsi/static/css/cookiebot.css?v=9.177.0" rel="stylesheet" />
            <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    
        <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
        <meta name="description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans.">
    
        <meta name="csrf-token" content="9de548adfd3c7270d237683ea4ea2b174d51689a95e7352bb2325fd5bdabc7df" />
        <meta property="og:site_name" content="
    CBCORP | CBCORP - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
    " />
        <meta property="og:image" content="https://cdn.robertsspaceindustries.com/static/images/RSI-fb.jpg" />
        <meta property="og:description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans." />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://robertsspaceindustries.com/en/citizens/CBCORP" />
        <meta property="og:locale" content="en" />
    
        <title>
    CBCORP | CBCORP - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
    </title>
    
        <link rel="canonical" href="https://robertsspaceindustries.com/en/citizens/CBCORP">
    
    
                      <link rel="alternate" href="https://robertsspaceindustries.com/en/citizens/CBCORP" hreflang="en">
    
    
            <link rel=preconnect href="//sentry.turbulent.ca">
        <link rel=preconnect href="//gstatic.com">
        <link rel=preconnect href="//www.recaptcha.net">
        <link rel=preconnect href="//www.googletagmanager.com">
    
    
            <link href="/rsi/static/css/rsi-minimal.css?v=9.177.0" media="all" rel="stylesheet">
    
    <link href="/rsi/static/css/cross-brand-less.css?v=9.177.0" media="all" rel="stylesheet">
    
    
    
    <script type="text/javascript" src="/cache/en/rsi-external-js.js?v=9.177.0"></script>
    <script type="text/javascript" src="/cache/en/rsi-templates-js.js?v=9.177.0"></script>
    
    
    
    <link rel="stylesheet" href="https://use.typekit.net/dhw3beb.css">
    
    
    
    
    <script type="text/javascript" src='/rsi/static/packages/core/rsi.core.build.e8130.js'></script>
    <script type="text/javascript" src='/rsi/static/packages/account/rsi.account.build.74772.js'></script>
    <script type="text/javascript" src='/rsi/static/packages/store/rsi.store.build.0278b.js'></script>
    
    <script>
    
        $(document).ready(function() {
        window.Common = new RSI.Common({});
        window.Main = new RSI.Main({
            'is_mobile': 0,
            'probation_cookie' : '',
            'require_captcha': 0
        });
        window.Mark = new Turbulent.Mark({ 'name' : 'Rsi-XSRF', 'token' : 'fnYPaA:YFRmbA36whYtFFyapkmd1w', 'ttl' : 1800 });
    
        window.WscOverlay = new RSI.WscOverlay({});
    
        var destinations = [];
    
    window.Main.destinations = destinations;
    
    
        });
    
        $(window).load(function() {
    
        });
    </script>
    
    
        <script>
        window.recaptcha_is_loaded = false;
        window.on_recaptcha_load_callback = function() {
        window.recaptcha_is_loaded = true;
        };
    </script>
    
    <script
        src="https://www.recaptcha.net/recaptcha/enterprise.js?onload=on_recaptcha_load_callback&render=6LerBOgUAAAAAKPg6vsAFPTN66Woz-jBClxdQU-o"
        async defer>
    </script>
        <script type="text/javascript">
    
        </script>
    
    
    
    
      <style>
    
          background:url(https://cdn.robertsspaceindustries.com/static/images/noisebg.gif) repeat center top #000b11;
    
      </style>
    
        <link href="https://robertsspaceindustries.com/rsi/assets/fonts.css?family=Electrolize|Orbitron:400,500,700|Quantico|Share+Tech+Mono" rel="stylesheet" type="text/css">
    
        <link href="/cache/en/rsi-css.css?v=9.177.0" media="all" rel="stylesheet">
    
    
        <script
        type="module"
        data-cookieconsent="ignore"
        src="https://robertsspaceindustries.com/plt-client/plt-client.es.js"
        data-platform-client-props="{&quot;lang&quot;:&quot;en&quot;,&quot;user&quot;:{&quot;isSignedIn&quot;:true,&quot;avatar&quot;:&quot;\/media\/0rixm629l5bwwr\/avatar\/A5ce2752-Ce33-446e-Ae18-2dab9f9ead8a.jpg&quot;,&quot;referral&quot;:{&quot;referralCode&quot;:&quot;STAR-73KP-54LB&quot;,&quot;referralUrl&quot;:&quot;https%3A%2F%2Frobertsspaceindustries.com%2Fenlist%3Freferral%3DSTAR-73KP-54LB&quot;,&quot;referralUrlCopy&quot;:&quot;https:\/\/robertsspaceindustries.com\/enlist?referral=STAR-73KP-54LB&quot;},&quot;useLegacyAccountPanel&quot;:false,&quot;isSubscriber&quot;:false,&quot;favorite&quot;:{&quot;img&quot;:&quot;https:\/\/media.robertsspaceindustries.com\/9qvh53v4nyx8d\/heap_note.png&quot;,&quot;name&quot;:&quot;Civilian&quot;},&quot;xsrfToken&quot;:{&quot;cookieName&quot;:&quot;Rsi-XSRF&quot;,&quot;token&quot;:&quot;fnYPaA:YFRmbA36whYtFFyapkmd1w&quot;,&quot;ttlMargin&quot;:1800000,&quot;cookieValue&quot;:null}}}"
    ></script>
      </head>
    
        <body id="" class=""  lang=en localized=1>
    
          <div
      data-rsi-component="Platform.Notification"
      data-rsi-component-props='{
        "id":"145",
        "type": "announcement",
        "severity": "P",
        "title":"Fly For Free",
        "content":"Play Star Citizen for FREE until April 28 and test fly 6 legendary ships!",
        "url":"https://robertsspaceindustries.com/en/flyfree"
      }'
    ></div>
    
    
    
    
    <div
      data-rsi-component="PlatformBar.Data"
      data-rsi-component-props='{
        "root": "home",
        "active": "dyn_bd_first_level_CBCORP",
        "api": {
          "nav": {
            "url": "/nav/",
            "load": ["main","games","shop","explore","community","support","tools"]
          }
        },
        "nodes": {
                      "dyn_bd_first_level_CBCORP": {"slug":"dyn_bd_first_level_CBCORP","parent":"home","item":{"title":"CBCORP"}},
                      "home": {
            "toolbar": ["launcher-link"]
          },
                "buy-star-citizen": {
            "item": {
              "link": {
                "href": "\/download"
              }
            }
          },
          "subscribers": {"children":["subscription-become","subscribers-store"]},
          "subscribers-store": {"item":{"link":{"href":"\/store\/pledge\/browse\/extras\/subscribers-store"}}},
          "subscription": {"item":{"link":{"href":"\/pledge\/subscriptions"}}}
        },
        "layouts": {
          "store-all": null
        },
        "localeSelector": {
          "available": {
            "languages": ["en"]
          },
          "selected": {
            "language": "en"
          }
                ,"languages": {"en":{"code":"en","label":"English","codeLabel":"en","subLabel":null,"altCodes":null,"badges":[],"url":"\/en\/citizens\/CBCORP"}}
                      ,"currency": {"USD":{"iso":"USD","symbol":"$","label":"United States dollar"},"CAD":{"iso":"CAD","symbol":"$","label":"Canadian dollar"},"EUR":{"iso":"EUR","symbol":"\u20ac","label":"Euro"},"GBP":{"iso":"GBP","symbol":"\u00a3","label":"Pound sterling"}}
              },
            "tools": {
          "launcher-link": {
            "title": "Download",
            "href": "\/download"
          }
        },
        "translations": {
          "backToRSIMobile": "BACK TO RSI.com",
          "cancelButton": "Cancel",
          "confirmButton": "Confirm",
          "currencyTitle": "Currency",
          "languageTitle": "Language"
        }
      }'>
    </div>
    
    <div
        data-rsi-component="PlatformBar.Head"
        data-rsi-component-props='{
            "breadCrumbCurrentItem": null    }'
        data-orion-skin="default"
        data-orion-theme=""
    ></div>
    
      <div
        data-rsi-component="PlatformBar.Navigation"
        data-orion-skin="default"
        data-orion-theme=""
      ></div>
    
    
        <div id="bodyWrapper">
                <div id="platform-client-root"></div>
    
    
      <div class="page-wrapper">
    
        <div id="contentbody" class="public-profile public-profile-landing" style="">
    
      <div id="profile" class="wrapper">
        <h1 class="page-title ">
      <span class="top-line"></span>
      <span class="inner-line"></span>
      <span class="icon"></span>CITIZEN DOSSIER
      <span class="bottom-line"></span>
    </h1>    <div id="public-profile" class="account-profile">
              <div class="tabs tabs2">
            <div class="holder clearfix">
              <a href="/citizens/CBCORP" class="holotab active">
                <span class="text trans-02s">Overview</span>
                <span class="top trans-02s"></span>
                <span class="bottom trans-02s"></span>
              </a>
              <a href="/citizens/CBCORP/organizations" class="holotab right">
                <span class="text trans-02s">Organizations</span>
                <span class="top trans-02s"></span>
                <span class="bottom trans-02s"></span>
              </a>
            </div>
          </div>
          <div class="profile-content overview-content clearfix">
            <p class="entry citizen-record">
              <span class="label">UEE Citizen Record</span>
              <strong class="value">n/a</strong>
            </p>
            <div class="box-content profile-wrapper clearfix">
              <div class="inner-bg clearfix">
                <div class="profile left-col">
                  <span class="title">Profile <a href="/account/profile" class="slashed-button edit">
      <span class="line l trans-02s"></span>
      <span class="line r trans-02s"></span>
      <span class="text trans-02s">Edit</span>
    </a>
    </span>
                  <div class="inner clearfix">
                    <div class="thumb">
                      <img src="/media/0rixm629l5bwwr/heap_infobox/A5ce2752-Ce33-446e-Ae18-2dab9f9ead8a.jpg" />
                      <span class="deco-corner top left"></span>
                      <span class="deco-corner top right"></span>
                      <span class="deco-corner bottom left"></span>
                      <span class="deco-corner bottom right"></span>
                    </div>
                    <div class="info">
                      <p class="entry">
                        <strong class="value">CBCORP</strong>
                      </p>
                      <p class="entry">
                        <span class="label">Handle name</span>
                        <strong class="value">CBCORP</strong>
                      </p>
                                          <p class="entry">
                                                  <span class="icon">
                              <img src="https://media.robertsspaceindustries.com/9qvh53v4nyx8d/heap_thumb.png"/>
                            </span>
                                                <span class="value">Civilian</span>
                        </p>
                                      </div>
                  </div>
                </div>
                <div class="main-org right-col visibility-">
                  <span class="title">Main organization <a href="/account/organization" class="slashed-button edit">
      <span class="line l trans-02s"></span>
      <span class="line r trans-02s"></span>
      <span class="text trans-02s">Edit</span>
    </a>
    </span>
                  <div class="inner clearfix">
                                      <div class="empty">NO MAIN ORG FOUND IN PUBLIC RECORDS</div>
                                  </div>
                  <span class="deco-separator top"></span>
                  <span class="deco-separator bottom"></span>
                              </div>
              </div>
              <span class="deco-corner top left"></span>
              <span class="deco-corner top right"></span>
              <span class="deco-corner bottom left"></span>
              <span class="deco-corner bottom right"></span>
              <span class="deco-edge left"><span class="top"></span><span class="bottom"></span></span>
              <span class="deco-edge right"><span class="top"></span><span class="bottom"></span></span>
            </div>
            <div class="left-col">
              <div class="inner">
                <p class="entry">
                  <span class="label">Enlisted</span>
                  <strong class="value">Feb 17, 2021</strong>
                </p>
                            <p class="entry">
                  <span class="label">Fluency</span>
                  <strong class="value">                                                  English                                </strong>
                </p>
              </div>
            </div>
            <div class="right-col">
              <div class="inner">
                                                                </div>
            </div>
                  </div>
        </div>
      </div>
    
        </div>
    
      </div>
    
    
    
    
    
                   <script id="tpl_number_counter_digits" type="text/x-jsmart-tmpl">{if !$seperator}{$seperator=','}{/if}
    {if !$first_max}{$first_max=9}{/if}
    {for $digit = 0 to $length-1}
      <div class="mask">
        <div class="carousel">
          {if $digit == 0}
            {$max = $first_max}
          {else}
            {$max = 9}
          {/if}
          {for $i=0 to $max}
            <div class="item {if $val_arr[$digit] == $i}on{/if}" rel="{$i}">{$i}</div>
          {/for}
        </div>
      </div>
      {if ($length - $digit) % 3 == 1 && $digit != $length-1}
      <div class="seperator">{$seperator}</div>
      {/if}
    {/for}</script>
    <script id="base_modal" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
      <div class="top-border">
        {block name="modal_lines"}
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        {/block}
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        {block name="modal_content"}{/block}
        {block name="modal_footer"}{/block}
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
        {block name="modal_lines"}
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        {/block}
      </div>
    </div></script>
    <script id="base_modal_flat" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
    
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        {block name="modal_content"}{/block}
        {block name="modal_footer"}{/block}
      </div>
    
    </div></script>
    <script id="tpl_modals_slideshow" type="text/x-jsmart-tmpl"><img class="top-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_top.png">
    <a href="" class="close js-close"></a>
    <div class="mask">
      <a class="js-prev prev control"></a>
      <a class="js-next next control"></a>
      <div class="slideshow-carousel carousel" rel="{$index}">
        {foreach from=$images item="image"}
          <div class="{if $index == $image@index}on{/if}">
          {if $image.is_video}
            <div class="video-holder">
              <div id="slideshow_video_{$image@index}" data-source="{$image->source_url}">
                <video width="100%" height="100%" preload="auto" {if $video}src="{$image->source_url}"{/if} controls></video>
              </div>
            </div>
          {else}
            <div class="media js-media-slideshow-{$image@iteration}">
            {if $image.low_res}
              <picture>
                <!--[if IE 9]><video style="display: none;"><![endif]-->
                <source data-srcset="{$image.full_res}" media="(min-width: 300px)" />
                <!--[if IE 9]></video><![endif]-->
                <img data-srcset="{$image.low_res}" alt="{$image.title}" />
              </picture>
            {else}
              <img data-src="{$image.source_url}" />
            {/if}
            </div>
          {/if}
            <div class="text">
              {if !$image.is_video}
              <a href="{$image.source_url}" class="download"></a>
              {/if}
              <div class="copyright">© 2012-{$year}<br />Cloud Imperium Games Corporation &<br />Roberts Space Industries Corp.</div>
              <div class="page-number">{$image@iteration} / {count($images)}</div>
              <div class="caption v-center">{if $image.title && $image.title != "undefined"}{$image.title}{/if}</div>
              <div class="cboth"></div>
            </div>
          </div>
        {/foreach}
      </div>
    </div>
    <img class="bottom-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_bottom.png"></script>
    <script id="tpl_contact_us" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
      <div class="top-border">
    
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
    
    <div id="contact" class="inner-content on">
      <h2><span class="icon"></span>CONTACT</h2>
      <div class="padder">
        <div class="separator"></div>
        <form name="" action="" method="POST" class="legacy-form">
      <div class="error-message js-error-message"></div>
      <div class="success-message js-success-message"></div>
        <fieldset>
        <label for="contact_subject">Subject</label>
        <input type="text" name="subject" value="" class="trans-02s trans-color trans-box-shadow" id="contact_subject" />
        <label>Contacting us for:</label>
        <ul class="category-info">
                <li id="tech_support_info">Questions about download, installation, networking, or in-game client problems</li>
                <li id="subscription_info">Questions about monthly and yearly subscription plans</li>
                <li id="account_billing_info">Issues related to your account, such as incorrect information or ability to access account, or Billing with regards to payments and payment methods</li>
                <li id="melt_request_info">To reclaim a pledge over $1,000 for store credit (please note - this is a permanent action)</li>
                <li id="merchandise_info">Questions about physical and/or shipped merchandise</li>
                <li id="hacked_info">Issues related to compromised account or missing pledge.</li>
                <li id="account_recovery_info">For issues with account authentication, lost passwords and related queries</li>
                <li id="probation_info">Issues related to forums probation or ban</li>
                <li id="refund_request_info">Refund requests and related inquiries</li>
                <li id="customer_support_info">For general questions and queries regarding Star Citizen</li>
              </ul>
      </fieldset>
      <fieldset>
        <label for="contact_text">Description</label>
        <textarea name="text" class="trans-02s trans-color trans-box-shadow" id="contact_text"></textarea>
      </fieldset>
      <div class="contact-submit-wrapper">
        <div class="line"></div>
        <button class="submit js-submit"><strong>submit your message</strong></button>
      </div>
    </form>
        <div class="separator"></div>
      </div>
    </div>
    
    
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
    
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    
      </div>
    </div></script>
    <script id="tpl_error" type="text/x-jsmart-tmpl"><div class="modal-error js-modal-error">
      <p class="modal-text js-modal-text"></p>
      <a class="close js-close trans-03s .trans-opacity" href=""></a>
    </div></script>
    <script id="tpl_success" type="text/x-jsmart-tmpl"><div class="modal-success js-modal-success">
      <p class="modal-text js-modal-text"></p>
      <a class="close js-close trans-03s .trans-opacity" href=""></a>
    </div></script>
    <script id="tpl_progress" type="text/x-jsmart-tmpl"><div class="modal-progress js-modal-progress">
      <div class="traj-loader">
        <div class="fast-blink"></div>
        <span class="modal-text js-modal-text"></span>
      </div>
    </div></script>
    <script id="tpl_outbound" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
      <div class="top-border">
    
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
    
    <div id="outbound" class="inner-content on">
      <h2><span class="icon"></span>OUTBOUND LINK</h2>
      <div class="padder">
        <div class="separator"></div>
        <form name="" action="" method="POST" class="legacy-form">
          <div class="error-message js-error-message"> <span class=important>WARNING</span><br/><br/> This link will bring you outside of the RSI site and into the depths of the internet. Continue?<br/><br/><span class="url"></span> </div>
          <div class="success-message js-success-message"><span class=important>STAND BY</span><br/><br/> Initiating hyperlink.<br/><br/></div>
    
          <fieldset class="clearfix last">
            <span class="submit-wrapper">
              <span class="submit-hover trans-02s trans-opacity"></span>
              <input type="submit" value="WARP" class="trans-02s trans-color trans-background" />
            </span>
          </fieldset>
        </form>
        <div class="separator"></div>
      </div>
    </div>
    
    
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
    
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    
      </div>
    </div></script>
    
    <script id="tpl_l-notification-bar" type="text/x-jsmart-tmpl"><div class="l-notification-bar js-notification-bar">
    
      <div class="l-notification-bar__watermark js-svg-inliner h-svg__logo-star-citizen"></div>
    
      <div class="l-notification-bar__boxes">
        {if !$viewedCookieNotif}
          <div class="l-notification-bar__box">
            {include file='tpl_c-notification'
              type='cookie'
              title='COOKIES:'
              message="Our website uses Google Analytics to analyze our traffic. <br/>To learn how you can control Google's use of your data and how you can opt out <a href='https://www.google.com/policies/privacy/partners/'>click here</a>."
              linkText='See Details'
              buttonText='Got it!'}
          </div>
        {/if}
    
        {if !$viewedPrivacyNotif}
          <div class="l-notification-bar__box">
            {include file='tpl_c-notification'
              type='privacy'
              title='PRIVACY POLICY:'
              message='We adjusted the PP to reflect the decision of the European Court of Justice regarding Safe Harbor, the fact that RSI has moved and added some services providers.'
              linkText='View Privacy Policy'
              buttonText='Got it!'}
          </div>
        {/if}
      </div>
    
    </div>
    </script>
    <script id="tpl_c-notification" type="text/x-jsmart-tmpl"><div class="c-notification js-bottom-notif-msg-{$type}">
        <div class="c-notification__title">{$title}</div>
        <div class="c-notification__message">
          {$message}
        </div>
    
        {if $linkText}
            <div class="c-notification__wrapper-link">
                <a class="c-notification__link js-bottom-notif-link-{$type}">
                {$linkText}
                </a>
            </div>
        {/if}
    
        <a class="c-notification__button js-bottom-notif-btn-{$type}">
    
          <span class="c-notification__button-text">
           {$buttonText}
          </span>
    
          {if $type neq 'announcement'}
            <div class="c-iconed__icon c-iconed__icon--checkmark"></div>
          {/if}
        </a>
    </div>
    </script>
    
    <script id="tpl_confirm" type="text/x-jsmart-tmpl"><div class="modal-confirm js-modal-confirm clearfix">
      <p class="modal-text js-modal-text"></p>
      <a class="bt-close js-close trans-03s trans-opacity" href=""></a>
      <a class="bt-confirm js-confirm trans-03s trans-opacity" href=""></a>
        <div class="buttons">
            <a class="shadow-button trans-02s trans-color js-close bt-close rm"     >
      <span class="label js-label trans-02s">Cancel</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
            <a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
      <span class="label js-label trans-02s">Confirm</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
        </div>
    </div>
    </script>
    <script id="tpl_alert" type="text/x-jsmart-tmpl"><div class="modal-alert js-modal-alert clearfix">
      <p class="modal-text js-modal-text"></p>
      <div class="buttons">
        <a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
      <span class="label js-label trans-02s">OK</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
      </div>
    </div></script>
    <script id="tpl_video" type="text/x-jsmart-tmpl">{extends file="base_modal"}
    {block name='modal_content'}
    <div id="ship-commercial" class="inner-content">
    
      <div class="hr"></div>
      <div class="content-block4">
    
        <div class="bottom"></div>
      </div>
      {if $distant_source=="vimeo"}
      <iframe id="commercial" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="//player.vimeo.com/video/{$video_id}?wmode=transparent" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>
      {else}
      <iframe id="commercial" frameborder="0" allowfullscreen="1" title="YouTube video player" width="100%" height="100%" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="https://www.youtube.com/embed/{$video_id}?autoplay=1"></iframe>
      {/if}
    </div>
    {/block}
    </script>
    
    
    
    
    
    
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KHNFZPT"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->
    
    
    <div data-rsi-component="PlatformFooter" data-rsi-component-props='{
      "currentSection": "rsi",
      "wscAbout": "/star-citizen",
      "wscPlay": "/playstarcitizen",
      "s42Game": "/squadron42",
      "s42Enlist": "/squadron42#enlist",
      "rsiCommlink": "/comm-link",
      "rsiCommunity": "/community-hub",
      "rsiRoadmap": "/roadmap",
      "showStoreMenu": "1",
      "isStoreMenuActive": "",
      "rsiStore": "/pledge",
      "rsiDownload": "/download",
      "isLauncherMenuActive": "",
      "rsiSpectrum": "/spectrum/community/SC",
      "showCitizenconMenu": "1",
      "rsiCitizencon": "/citizencon",
      "utilitiesHelp": "//support.robertsspaceindustries.com",
      "utilitiesPress": "/press",
      "utilitiesCareers": "https://cloudimperiumgames.com/join-us",
      "utilitiesAcknowledgement": "/acknowledgements",
      "utilitiesRedeemCode": "/pledge/redeem-code",
      "legalLegal": "/legal",
      "legalTos": "/tos",
      "legalPrivacy": "/privacy",
      "legalEula": "/eula",
      "legalDmca": "/dmca",
      "legalDisclosure": "/responsible-disclosure",
      "legalCaliforniaLegalNoticeAtCollection": "/privacy#california",
      "legalCaliforniaLegalPersonalInformation": "/cookies#preferences",
      "isConsentRequired": "",
      "clientRecordCountry": "GB",
      "cigLink": "https://cloudimperiumgames.com",
      "displayStarEngine": ""
    }'></div>
    
        </div>
      </body>
    </html>
"""


@pytest.fixture
def pilot_with_corp_and_location_profile():
    return """
    <!DOCTYPE html>
        
    <html lang="en">
      <head>
            
        <script
        id="TagManager"
        data-cookieconsent="ignore"
        data-app-name="rsi-heap"
        data-app-version="9.177.0"
        data-category="account"
        data-sub-category="account-profile-public"
        src="/tag-manager/script.js"
        type="text/javascript"></script>
            <script
        type="text/javascript"
        id="Cookiebot"
        src="https://consent.cookiebot.com/uc.js"
        data-cbid="a687ee30-df65-45a0-9d22-90de6c1bb964"
        data-blockingmode="auto"
        data-georegions="{'region':'US-06,US-51,AT,BE,BG,HR,CY,CZ,DK,EE,FI,FR,DE,GR,HU,IE,IT,LV,LT,LU,MT,NL,PL,PT,RO,SK,SL,ES,SE','cbid':'a687ee30-df65-45a0-9d22-90de6c1bb964'}"></script>
        <script id="CookieConsent" src="/cookie-consent/script.js?async=false" type="text/javascript"></script>
      <link href="/rsi/static/css/cookiebot.css?v=9.177.0" rel="stylesheet" />
            <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    
        <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
        <meta name="description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans.">
    
        <meta name="csrf-token" content="9de548adfd3c7270d237683ea4ea2b174d51689a95e7352bb2325fd5bdabc7df" />
        <meta property="og:site_name" content="
    Turz1- | Tur0 - SCS | SCSFIN (Master) - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
    " />
        <meta property="og:image" content="https://cdn.robertsspaceindustries.com/static/images/RSI-fb.jpg" />
        <meta property="og:description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans." />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://robertsspaceindustries.com/en/citizens/Tur0" />
        <meta property="og:locale" content="en" />
    
        <title>
    Turz1- | Tur0 - SCS | SCSFIN (Master) - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
    </title>
    
        <link rel="canonical" href="https://robertsspaceindustries.com/en/citizens/Tur0">
    
        
                      <link rel="alternate" href="https://robertsspaceindustries.com/en/citizens/Tur0" hreflang="en">
                                
    
            <link rel=preconnect href="//sentry.turbulent.ca">
        <link rel=preconnect href="//gstatic.com">
        <link rel=preconnect href="//www.recaptcha.net">
        <link rel=preconnect href="//www.googletagmanager.com">
          
    
            <link href="/rsi/static/css/rsi-minimal.css?v=9.177.0" media="all" rel="stylesheet">
        
    <link href="/rsi/static/css/cross-brand-less.css?v=9.177.0" media="all" rel="stylesheet">
    
    
              
    <script type="text/javascript" src="/cache/en/rsi-external-js.js?v=9.177.0"></script>
    <script type="text/javascript" src="/cache/en/rsi-templates-js.js?v=9.177.0"></script>
    
            
              
    <link rel="stylesheet" href="https://use.typekit.net/dhw3beb.css">
    
    
    
              
    <script type="text/javascript" src='/rsi/static/packages/core/rsi.core.build.e8130.js'></script>
    <script type="text/javascript" src='/rsi/static/packages/account/rsi.account.build.74772.js'></script>
    <script type="text/javascript" src='/rsi/static/packages/store/rsi.store.build.0278b.js'></script>
    
    <script>
                    
        $(document).ready(function() {
        window.Common = new RSI.Common({});
        window.Main = new RSI.Main({
            'is_mobile': 0,
            'probation_cookie' : '',
            'require_captcha': 0
        });
        window.Mark = new Turbulent.Mark({ 'name' : 'Rsi-XSRF', 'token' : 'K34PaA:iDtXrIH3XX0NOZzjj0Lcjg', 'ttl' : 1800 });
    
        window.WscOverlay = new RSI.WscOverlay({});
    
        var destinations = [];
    
    window.Main.destinations = destinations;    
        
        
        });
    
        $(window).load(function() {
        
        });
    </script>
    
    
        <script>
        window.recaptcha_is_loaded = false;
        window.on_recaptcha_load_callback = function() {
        window.recaptcha_is_loaded = true;
        };
    </script>
    
    <script
        src="https://www.recaptcha.net/recaptcha/enterprise.js?onload=on_recaptcha_load_callback&render=6LerBOgUAAAAAKPg6vsAFPTN66Woz-jBClxdQU-o"
        async defer>
    </script>
        <script type="text/javascript">
          
        </script>
    
        
    
        
      <style>
        
          background:url(https://cdn.robertsspaceindustries.com/static/images/noisebg.gif) repeat center top #000b11;
        
      </style>
    
        <link href="https://robertsspaceindustries.com/rsi/assets/fonts.css?family=Electrolize|Orbitron:400,500,700|Quantico|Share+Tech+Mono" rel="stylesheet" type="text/css">
    
        <link href="/cache/en/rsi-css.css?v=9.177.0" media="all" rel="stylesheet">
    
    
        <script 
        type="module" 
        data-cookieconsent="ignore" 
        src="https://robertsspaceindustries.com/plt-client/plt-client.es.js"
        data-platform-client-props="{&quot;lang&quot;:&quot;en&quot;,&quot;user&quot;:{&quot;isSignedIn&quot;:true,&quot;avatar&quot;:&quot;\/media\/0rixm629l5bwwr\/avatar\/A5ce2752-Ce33-446e-Ae18-2dab9f9ead8a.jpg&quot;,&quot;referral&quot;:{&quot;referralCode&quot;:&quot;STAR-73KP-54LB&quot;,&quot;referralUrl&quot;:&quot;https%3A%2F%2Frobertsspaceindustries.com%2Fenlist%3Freferral%3DSTAR-73KP-54LB&quot;,&quot;referralUrlCopy&quot;:&quot;https:\/\/robertsspaceindustries.com\/enlist?referral=STAR-73KP-54LB&quot;},&quot;useLegacyAccountPanel&quot;:false,&quot;isSubscriber&quot;:false,&quot;favorite&quot;:{&quot;img&quot;:&quot;https:\/\/media.robertsspaceindustries.com\/9qvh53v4nyx8d\/heap_note.png&quot;,&quot;name&quot;:&quot;Civilian&quot;},&quot;xsrfToken&quot;:{&quot;cookieName&quot;:&quot;Rsi-XSRF&quot;,&quot;token&quot;:&quot;K34PaA:iDtXrIH3XX0NOZzjj0Lcjg&quot;,&quot;ttlMargin&quot;:1800000,&quot;cookieValue&quot;:null}}}"
    ></script>
      </head>
    
        <body id="" class=""  lang=en localized=1>
        
          <div
      data-rsi-component="Platform.Notification"
      data-rsi-component-props='{
        "id":"145",
        "type": "announcement",
        "severity": "P",
        "title":"Fly For Free",
        "content":"Play Star Citizen for FREE until April 28 and test fly 6 legendary ships!",
        "url":"https://robertsspaceindustries.com/en/flyfree"
      }'
    ></div>
        
    
        
                
    <div 
      data-rsi-component="PlatformBar.Data"
      data-rsi-component-props='{
        "root": "home",
        "active": "dyn_bd_first_level_Tur0",
        "api": {
          "nav": {
            "url": "/nav/",
            "load": ["main","games","shop","explore","community","support","tools"]
          }
        },
        "nodes": {
                      "dyn_bd_first_level_Tur0": {"slug":"dyn_bd_first_level_Tur0","parent":"home","item":{"title":"Tur0"}},
                      "home": {
            "toolbar": ["launcher-link"]
          },
                "buy-star-citizen": {
            "item": {
              "link": {
                "href": "\/download"
              }
            }
          },
          "subscribers": {"children":["subscription-become","subscribers-store"]},
          "subscribers-store": {"item":{"link":{"href":"\/store\/pledge\/browse\/extras\/subscribers-store"}}},
          "subscription": {"item":{"link":{"href":"\/pledge\/subscriptions"}}}
        },
        "layouts": {
          "store-all": null
        },
        "localeSelector": {
          "available": {
            "languages": ["en"]
          },
          "selected": {
            "language": "en"
          }
                ,"languages": {"en":{"code":"en","label":"English","codeLabel":"en","subLabel":null,"altCodes":null,"badges":[],"url":"\/en\/citizens\/Tur0"}}
                      ,"currency": {"USD":{"iso":"USD","symbol":"$","label":"United States dollar"},"CAD":{"iso":"CAD","symbol":"$","label":"Canadian dollar"},"EUR":{"iso":"EUR","symbol":"\u20ac","label":"Euro"},"GBP":{"iso":"GBP","symbol":"\u00a3","label":"Pound sterling"}}
              },
            "tools": {
          "launcher-link": {
            "title": "Download",
            "href": "\/download"
          }
        },
        "translations": {
          "backToRSIMobile": "BACK TO RSI.com",
          "cancelButton": "Cancel",
          "confirmButton": "Confirm",
          "currencyTitle": "Currency",
          "languageTitle": "Language"
        }
      }'>
    </div>
    
    <div
        data-rsi-component="PlatformBar.Head"
        data-rsi-component-props='{
            "breadCrumbCurrentItem": null    }'
        data-orion-skin="default"
        data-orion-theme=""
    ></div>
    
      <div
        data-rsi-component="PlatformBar.Navigation"
        data-orion-skin="default"
        data-orion-theme=""
      ></div>
        
    
        <div id="bodyWrapper">
                <div id="platform-client-root"></div>
          
        
      <div class="page-wrapper">
        
        <div id="contentbody" class="public-profile public-profile-landing" style="">
          
      <div id="profile" class="wrapper">
        <h1 class="page-title ">
      <span class="top-line"></span>
      <span class="inner-line"></span>
      <span class="icon"></span>CITIZEN DOSSIER
      <span class="bottom-line"></span>
    </h1>    <div id="public-profile" class="account-profile">
              <div class="tabs tabs2">
            <div class="holder clearfix">
              <a href="/citizens/Tur0" class="holotab active">
                <span class="text trans-02s">Overview</span>
                <span class="top trans-02s"></span>
                <span class="bottom trans-02s"></span>
              </a>
              <a href="/citizens/Tur0/organizations" class="holotab right">
                <span class="text trans-02s">Organizations</span>
                <span class="top trans-02s"></span>
                <span class="bottom trans-02s"></span>
              </a>
            </div>
          </div>
          <div class="profile-content overview-content clearfix">
            <p class="entry citizen-record">
              <span class="label">UEE Citizen Record</span>
              <strong class="value">#1801846</strong>
            </p>
            <div class="box-content profile-wrapper clearfix">
              <div class="inner-bg clearfix">
                <div class="profile left-col">
                  <span class="title">Profile </span>
                  <div class="inner clearfix">
                    <div class="thumb">
                      <img src="https://cdn.robertsspaceindustries.com/static/images/account/avatar_default_big.jpg" />
                      <span class="deco-corner top left"></span>
                      <span class="deco-corner top right"></span>
                      <span class="deco-corner bottom left"></span>
                      <span class="deco-corner bottom right"></span>
                    </div>
                    <div class="info">
                      <p class="entry">
                        <strong class="value">Turz1-</strong>
                      </p>
                      <p class="entry">
                        <span class="label">Handle name</span>
                        <strong class="value">Tur0</strong>
                      </p>
                                          <p class="entry">
                                                  <span class="icon">
                              <img src="https://media.robertsspaceindustries.com/9qvh53v4nyx8d/heap_thumb.png"/>
                            </span>
                                                <span class="value">Civilian</span>
                        </p>
                                      </div>
                  </div>
                </div>
                <div class="main-org right-col visibility-V">
                  <span class="title">Main organization </span>
                  <div class="inner clearfix">
                                      <div class="thumb">
                                                                                      <a href="/orgs/SCSFIN"><img src="https://cdn.robertsspaceindustries.com/static/images/organization/defaults/logo/generic.jpg" /></a>
                                            <span class="deco-corner top left"></span>
                        <span class="deco-corner top right"></span>
                        <span class="deco-corner bottom left"></span>
                        <span class="deco-corner bottom right"></span>
                      </div>
                      <div class="info">
                        <p class="entry">
                                                <a href="/orgs/SCSFIN" class="value data3" style="background-position:-234px center">SCS</a>
                        </p>
                        <p class="entry">
                                                <span class="label data8">Spectrum Identification (SID)</span>
                                                <strong class="value data9">SCSFIN</strong>
                        </p>
                        <p class="entry">
                                                <span class="label data6">Organization rank</span>
                                                <strong class="value data15">Master</strong>
                        </p>
                        <div class="ranking data6">
                                                                            <span class="active"><span></span></span>
                                                      <span class="active"><span></span></span>
                                                      <span class="active"><span></span></span>
                                                      <span class="active"><span></span></span>
                                                      <span class="active"><span></span></span>
                                                                      </div>
                      </div>
                                  </div>
                  <span class="deco-separator top"></span>
                  <span class="deco-separator bottom"></span>
                              </div>
              </div>
              <span class="deco-corner top left"></span>
              <span class="deco-corner top right"></span>
              <span class="deco-corner bottom left"></span>
              <span class="deco-corner bottom right"></span>
              <span class="deco-edge left"><span class="top"></span><span class="bottom"></span></span>
              <span class="deco-edge right"><span class="top"></span><span class="bottom"></span></span>
            </div>
            <div class="left-col">
              <div class="inner">
                <p class="entry">
                  <span class="label">Enlisted</span>
                  <strong class="value">May 5, 2017</strong>
                </p>
                              <p class="entry">
                    <span class="label">Location</span>
                    <strong class="value">
                      Finland
                                          , Uusimaa
                                      </strong>
                  </p>
                            <p class="entry">
                  <span class="label">Fluency</span>
                  <strong class="value">                                                  English,                                  Finnish                                </strong>
                </p>
              </div>
            </div>
            <div class="right-col">
              <div class="inner">
                                                                </div>
            </div>
                  </div>
        </div>
      </div>
    
        </div>
        
      </div>
    
      
    
    
    
                   <script id="tpl_number_counter_digits" type="text/x-jsmart-tmpl">{if !$seperator}{$seperator=','}{/if}
    {if !$first_max}{$first_max=9}{/if}
    {for $digit = 0 to $length-1}
      <div class="mask">
        <div class="carousel">
          {if $digit == 0}
            {$max = $first_max}
          {else}
            {$max = 9}
          {/if}
          {for $i=0 to $max}
            <div class="item {if $val_arr[$digit] == $i}on{/if}" rel="{$i}">{$i}</div>
          {/for}
        </div>
      </div>
      {if ($length - $digit) % 3 == 1 && $digit != $length-1}
      <div class="seperator">{$seperator}</div>
      {/if}
    {/for}</script>
    <script id="base_modal" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
      <div class="top-border">
        {block name="modal_lines"}
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        {/block}
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        {block name="modal_content"}{/block}
        {block name="modal_footer"}{/block}
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
        {block name="modal_lines"}
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        {/block}
      </div>
    </div></script>
    <script id="base_modal_flat" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
      
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        {block name="modal_content"}{/block}
        {block name="modal_footer"}{/block}
      </div>
      
    </div></script>
    <script id="tpl_modals_slideshow" type="text/x-jsmart-tmpl"><img class="top-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_top.png">
    <a href="" class="close js-close"></a>
    <div class="mask">
      <a class="js-prev prev control"></a>
      <a class="js-next next control"></a>
      <div class="slideshow-carousel carousel" rel="{$index}">
        {foreach from=$images item="image"}
          <div class="{if $index == $image@index}on{/if}">
          {if $image.is_video}
            <div class="video-holder">
              <div id="slideshow_video_{$image@index}" data-source="{$image->source_url}">
                <video width="100%" height="100%" preload="auto" {if $video}src="{$image->source_url}"{/if} controls></video>
              </div>
            </div>
          {else}
            <div class="media js-media-slideshow-{$image@iteration}">
            {if $image.low_res}
              <picture>
                <!--[if IE 9]><video style="display: none;"><![endif]-->
                <source data-srcset="{$image.full_res}" media="(min-width: 300px)" />
                <!--[if IE 9]></video><![endif]-->
                <img data-srcset="{$image.low_res}" alt="{$image.title}" />
              </picture>
            {else}
              <img data-src="{$image.source_url}" />
            {/if}
            </div>
          {/if}
            <div class="text">
              {if !$image.is_video}
              <a href="{$image.source_url}" class="download"></a>
              {/if}
              <div class="copyright">© 2012-{$year}<br />Cloud Imperium Games Corporation &<br />Roberts Space Industries Corp.</div>
              <div class="page-number">{$image@iteration} / {count($images)}</div>
              <div class="caption v-center">{if $image.title && $image.title != "undefined"}{$image.title}{/if}</div>
              <div class="cboth"></div>
            </div>
          </div>
        {/foreach}
      </div>
    </div>
    <img class="bottom-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_bottom.png"></script>
    <script id="tpl_contact_us" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
      <div class="top-border">
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        
    <div id="contact" class="inner-content on">
      <h2><span class="icon"></span>CONTACT</h2>
      <div class="padder">
        <div class="separator"></div>
        <form name="" action="" method="POST" class="legacy-form">
      <div class="error-message js-error-message"></div>
      <div class="success-message js-success-message"></div>
        <fieldset>
        <label for="contact_subject">Subject</label>
        <input type="text" name="subject" value="" class="trans-02s trans-color trans-box-shadow" id="contact_subject" />
        <label>Contacting us for:</label>
        <ul class="category-info">
                <li id="tech_support_info">Questions about download, installation, networking, or in-game client problems</li>
                <li id="subscription_info">Questions about monthly and yearly subscription plans</li>
                <li id="account_billing_info">Issues related to your account, such as incorrect information or ability to access account, or Billing with regards to payments and payment methods</li>
                <li id="melt_request_info">To reclaim a pledge over $1,000 for store credit (please note - this is a permanent action)</li>
                <li id="merchandise_info">Questions about physical and/or shipped merchandise</li>
                <li id="hacked_info">Issues related to compromised account or missing pledge.</li>
                <li id="account_recovery_info">For issues with account authentication, lost passwords and related queries</li>
                <li id="probation_info">Issues related to forums probation or ban</li>
                <li id="refund_request_info">Refund requests and related inquiries</li>
                <li id="customer_support_info">For general questions and queries regarding Star Citizen</li>
              </ul>
      </fieldset>
      <fieldset>
        <label for="contact_text">Description</label>
        <textarea name="text" class="trans-02s trans-color trans-box-shadow" id="contact_text"></textarea>
      </fieldset>
      <div class="contact-submit-wrapper">
        <div class="line"></div>
        <button class="submit js-submit"><strong>submit your message</strong></button>
      </div>
    </form>
        <div class="separator"></div>
      </div>
    </div>
    
        
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
      </div>
    </div></script>
    <script id="tpl_error" type="text/x-jsmart-tmpl"><div class="modal-error js-modal-error">
      <p class="modal-text js-modal-text"></p>
      <a class="close js-close trans-03s .trans-opacity" href=""></a>
    </div></script>
    <script id="tpl_success" type="text/x-jsmart-tmpl"><div class="modal-success js-modal-success">
      <p class="modal-text js-modal-text"></p>
      <a class="close js-close trans-03s .trans-opacity" href=""></a>
    </div></script>
    <script id="tpl_progress" type="text/x-jsmart-tmpl"><div class="modal-progress js-modal-progress">
      <div class="traj-loader">
        <div class="fast-blink"></div>
        <span class="modal-text js-modal-text"></span>
      </div>
    </div></script>
    <script id="tpl_outbound" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
      <div class="top-border">
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        
    <div id="outbound" class="inner-content on">
      <h2><span class="icon"></span>OUTBOUND LINK</h2>
      <div class="padder">
        <div class="separator"></div>
        <form name="" action="" method="POST" class="legacy-form">
          <div class="error-message js-error-message"> <span class=important>WARNING</span><br/><br/> This link will bring you outside of the RSI site and into the depths of the internet. Continue?<br/><br/><span class="url"></span> </div>
          <div class="success-message js-success-message"><span class=important>STAND BY</span><br/><br/> Initiating hyperlink.<br/><br/></div>
    
          <fieldset class="clearfix last">
            <span class="submit-wrapper">
              <span class="submit-hover trans-02s trans-opacity"></span>
              <input type="submit" value="WARP" class="trans-02s trans-color trans-background" />
            </span>
          </fieldset>
        </form>
        <div class="separator"></div>
      </div>
    </div>
    
        
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
      </div>
    </div></script>
    
    <script id="tpl_l-notification-bar" type="text/x-jsmart-tmpl"><div class="l-notification-bar js-notification-bar">
    
      <div class="l-notification-bar__watermark js-svg-inliner h-svg__logo-star-citizen"></div>
    
      <div class="l-notification-bar__boxes">
        {if !$viewedCookieNotif}
          <div class="l-notification-bar__box">
            {include file='tpl_c-notification'
              type='cookie'
              title='COOKIES:'
              message="Our website uses Google Analytics to analyze our traffic. <br/>To learn how you can control Google's use of your data and how you can opt out <a href='https://www.google.com/policies/privacy/partners/'>click here</a>."
              linkText='See Details'
              buttonText='Got it!'}
          </div>
        {/if}
    
        {if !$viewedPrivacyNotif}
          <div class="l-notification-bar__box">
            {include file='tpl_c-notification'
              type='privacy'
              title='PRIVACY POLICY:'
              message='We adjusted the PP to reflect the decision of the European Court of Justice regarding Safe Harbor, the fact that RSI has moved and added some services providers.'
              linkText='View Privacy Policy'
              buttonText='Got it!'}
          </div>
        {/if}
      </div>
    
    </div>
    </script>
    <script id="tpl_c-notification" type="text/x-jsmart-tmpl"><div class="c-notification js-bottom-notif-msg-{$type}">
        <div class="c-notification__title">{$title}</div>
        <div class="c-notification__message">
          {$message}
        </div>
    
        {if $linkText}
            <div class="c-notification__wrapper-link">
                <a class="c-notification__link js-bottom-notif-link-{$type}">
                {$linkText}
                </a>
            </div>
        {/if}
    
        <a class="c-notification__button js-bottom-notif-btn-{$type}">
    
          <span class="c-notification__button-text">
           {$buttonText}
          </span>
    
          {if $type neq 'announcement'}
            <div class="c-iconed__icon c-iconed__icon--checkmark"></div>
          {/if}
        </a>
    </div>
    </script>
    
    <script id="tpl_confirm" type="text/x-jsmart-tmpl"><div class="modal-confirm js-modal-confirm clearfix">
      <p class="modal-text js-modal-text"></p>
      <a class="bt-close js-close trans-03s trans-opacity" href=""></a>
      <a class="bt-confirm js-confirm trans-03s trans-opacity" href=""></a>
        <div class="buttons">
            <a class="shadow-button trans-02s trans-color js-close bt-close rm"     >
      <span class="label js-label trans-02s">Cancel</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
            <a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
      <span class="label js-label trans-02s">Confirm</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
        </div>
    </div>
    </script>
    <script id="tpl_alert" type="text/x-jsmart-tmpl"><div class="modal-alert js-modal-alert clearfix">
      <p class="modal-text js-modal-text"></p>
      <div class="buttons">
        <a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
      <span class="label js-label trans-02s">OK</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
      </div>
    </div></script>
    <script id="tpl_video" type="text/x-jsmart-tmpl">{extends file="base_modal"}
    {block name='modal_content'}
    <div id="ship-commercial" class="inner-content">
    
      <div class="hr"></div>
      <div class="content-block4">
    
        <div class="bottom"></div>
      </div>
      {if $distant_source=="vimeo"}
      <iframe id="commercial" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="//player.vimeo.com/video/{$video_id}?wmode=transparent" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>
      {else}
      <iframe id="commercial" frameborder="0" allowfullscreen="1" title="YouTube video player" width="100%" height="100%" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="https://www.youtube.com/embed/{$video_id}?autoplay=1"></iframe>
      {/if}
    </div>
    {/block}
    </script>
          
    
          
            
        
    
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KHNFZPT"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->
    
    
    <div data-rsi-component="PlatformFooter" data-rsi-component-props='{
      "currentSection": "rsi",
      "wscAbout": "/star-citizen",
      "wscPlay": "/playstarcitizen",
      "s42Game": "/squadron42",
      "s42Enlist": "/squadron42#enlist",
      "rsiCommlink": "/comm-link",
      "rsiCommunity": "/community-hub",
      "rsiRoadmap": "/roadmap",
      "showStoreMenu": "1",
      "isStoreMenuActive": "",
      "rsiStore": "/pledge",
      "rsiDownload": "/download",
      "isLauncherMenuActive": "",
      "rsiSpectrum": "/spectrum/community/SC",
      "showCitizenconMenu": "1",
      "rsiCitizencon": "/citizencon",
      "utilitiesHelp": "//support.robertsspaceindustries.com",
      "utilitiesPress": "/press",
      "utilitiesCareers": "https://cloudimperiumgames.com/join-us",
      "utilitiesAcknowledgement": "/acknowledgements",
      "utilitiesRedeemCode": "/pledge/redeem-code",
      "legalLegal": "/legal",
      "legalTos": "/tos",
      "legalPrivacy": "/privacy",
      "legalEula": "/eula",
      "legalDmca": "/dmca",
      "legalDisclosure": "/responsible-disclosure",
      "legalCaliforniaLegalNoticeAtCollection": "/privacy#california",
      "legalCaliforniaLegalPersonalInformation": "/cookies#preferences",
      "isConsentRequired": "",
      "clientRecordCountry": "GB",
      "cigLink": "https://cloudimperiumgames.com",
      "displayStarEngine": ""
    }'></div>
          
        </div>
      </body>
    </html>

"""

@pytest.fixture
def pilot_with_custom_icon_profile():
    return """
    <!DOCTYPE html>
        
    <html lang="en">
      <head>
            
        <script
        id="TagManager"
        data-cookieconsent="ignore"
        data-app-name="rsi-heap"
        data-app-version="9.177.0"
        data-category="account"
        data-sub-category="account-profile-public"
        src="/tag-manager/script.js"
        type="text/javascript"></script>
            <script
        type="text/javascript"
        id="Cookiebot"
        src="https://consent.cookiebot.com/uc.js"
        data-cbid="a687ee30-df65-45a0-9d22-90de6c1bb964"
        data-blockingmode="auto"
        data-georegions="{'region':'US-06,US-51,AT,BE,BG,HR,CY,CZ,DK,EE,FI,FR,DE,GR,HU,IE,IT,LV,LT,LU,MT,NL,PL,PT,RO,SK,SL,ES,SE','cbid':'a687ee30-df65-45a0-9d22-90de6c1bb964'}"></script>
        <script id="CookieConsent" src="/cookie-consent/script.js?async=false" type="text/javascript"></script>
      <link href="/rsi/static/css/cookiebot.css?v=9.177.0" rel="stylesheet" />
            <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    
        <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
        <meta name="description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans.">
    
        <meta name="csrf-token" content="9de548adfd3c7270d237683ea4ea2b174d51689a95e7352bb2325fd5bdabc7df" />
        <meta property="og:site_name" content="
    Steinchen | Steinchen - Cooperative Industries | C0IN (Mitglied) - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
    " />
        <meta property="og:image" content="https://cdn.robertsspaceindustries.com/static/images/RSI-fb.jpg" />
        <meta property="og:description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans." />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://robertsspaceindustries.com/en/citizens/Steinchen" />
        <meta property="og:locale" content="en" />
    
        <title>
    Steinchen | Steinchen - Cooperative Industries | C0IN (Mitglied) - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
    </title>
    
        <link rel="canonical" href="https://robertsspaceindustries.com/en/citizens/Steinchen">
    
        
                      <link rel="alternate" href="https://robertsspaceindustries.com/en/citizens/Steinchen" hreflang="en">
                                
    
            <link rel=preconnect href="//sentry.turbulent.ca">
        <link rel=preconnect href="//gstatic.com">
        <link rel=preconnect href="//www.recaptcha.net">
        <link rel=preconnect href="//www.googletagmanager.com">
          
    
            <link href="/rsi/static/css/rsi-minimal.css?v=9.177.0" media="all" rel="stylesheet">
        
    <link href="/rsi/static/css/cross-brand-less.css?v=9.177.0" media="all" rel="stylesheet">
    
    
              
    <script type="text/javascript" src="/cache/en/rsi-external-js.js?v=9.177.0"></script>
    <script type="text/javascript" src="/cache/en/rsi-templates-js.js?v=9.177.0"></script>
    
            
              
    <link rel="stylesheet" href="https://use.typekit.net/dhw3beb.css">
    
    
    
              
    <script type="text/javascript" src='/rsi/static/packages/core/rsi.core.build.e8130.js'></script>
    <script type="text/javascript" src='/rsi/static/packages/account/rsi.account.build.74772.js'></script>
    <script type="text/javascript" src='/rsi/static/packages/store/rsi.store.build.0278b.js'></script>
    
    <script>
                    
        $(document).ready(function() {
        window.Common = new RSI.Common({});
        window.Main = new RSI.Main({
            'is_mobile': 0,
            'probation_cookie' : '',
            'require_captcha': 0
        });
        window.Mark = new Turbulent.Mark({ 'name' : 'Rsi-XSRF', 'token' : 'd4YPaA:ECfNNbgiI1BLqsHCe+a/iA', 'ttl' : 1800 });
    
        window.WscOverlay = new RSI.WscOverlay({});
    
        var destinations = [];
    
    window.Main.destinations = destinations;    
        
        
        });
    
        $(window).load(function() {
        
        });
    </script>
    
    
        <script>
        window.recaptcha_is_loaded = false;
        window.on_recaptcha_load_callback = function() {
        window.recaptcha_is_loaded = true;
        };
    </script>
    
    <script
        src="https://www.recaptcha.net/recaptcha/enterprise.js?onload=on_recaptcha_load_callback&render=6LerBOgUAAAAAKPg6vsAFPTN66Woz-jBClxdQU-o"
        async defer>
    </script>
        <script type="text/javascript">
          
        </script>
    
        
    
        
      <style>
        
          background:url(https://cdn.robertsspaceindustries.com/static/images/noisebg.gif) repeat center top #000b11;
        
      </style>
    
        <link href="https://robertsspaceindustries.com/rsi/assets/fonts.css?family=Electrolize|Orbitron:400,500,700|Quantico|Share+Tech+Mono" rel="stylesheet" type="text/css">
    
        <link href="/cache/en/rsi-css.css?v=9.177.0" media="all" rel="stylesheet">
    
    
        <script 
        type="module" 
        data-cookieconsent="ignore" 
        src="https://robertsspaceindustries.com/plt-client/plt-client.es.js"
        data-platform-client-props="{&quot;lang&quot;:&quot;en&quot;,&quot;user&quot;:{&quot;isSignedIn&quot;:true,&quot;avatar&quot;:&quot;\/media\/0rixm629l5bwwr\/avatar\/A5ce2752-Ce33-446e-Ae18-2dab9f9ead8a.jpg&quot;,&quot;referral&quot;:{&quot;referralCode&quot;:&quot;STAR-73KP-54LB&quot;,&quot;referralUrl&quot;:&quot;https%3A%2F%2Frobertsspaceindustries.com%2Fenlist%3Freferral%3DSTAR-73KP-54LB&quot;,&quot;referralUrlCopy&quot;:&quot;https:\/\/robertsspaceindustries.com\/enlist?referral=STAR-73KP-54LB&quot;},&quot;useLegacyAccountPanel&quot;:false,&quot;isSubscriber&quot;:false,&quot;favorite&quot;:{&quot;img&quot;:&quot;https:\/\/media.robertsspaceindustries.com\/9qvh53v4nyx8d\/heap_note.png&quot;,&quot;name&quot;:&quot;Civilian&quot;},&quot;xsrfToken&quot;:{&quot;cookieName&quot;:&quot;Rsi-XSRF&quot;,&quot;token&quot;:&quot;d4YPaA:ECfNNbgiI1BLqsHCe+a\/iA&quot;,&quot;ttlMargin&quot;:1800000,&quot;cookieValue&quot;:null}}}"
    ></script>
      </head>
    
        <body id="" class=""  lang=en localized=1>
        
          <div
      data-rsi-component="Platform.Notification"
      data-rsi-component-props='{
        "id":"145",
        "type": "announcement",
        "severity": "P",
        "title":"Fly For Free",
        "content":"Play Star Citizen for FREE until April 28 and test fly 6 legendary ships!",
        "url":"https://robertsspaceindustries.com/en/flyfree"
      }'
    ></div>
        
    
        
                
    <div 
      data-rsi-component="PlatformBar.Data"
      data-rsi-component-props='{
        "root": "home",
        "active": "dyn_bd_first_level_Steinchen",
        "api": {
          "nav": {
            "url": "/nav/",
            "load": ["main","games","shop","explore","community","support","tools"]
          }
        },
        "nodes": {
                      "dyn_bd_first_level_Steinchen": {"slug":"dyn_bd_first_level_Steinchen","parent":"home","item":{"title":"Steinchen"}},
                      "home": {
            "toolbar": ["launcher-link"]
          },
                "buy-star-citizen": {
            "item": {
              "link": {
                "href": "\/download"
              }
            }
          },
          "subscribers": {"children":["subscription-become","subscribers-store"]},
          "subscribers-store": {"item":{"link":{"href":"\/store\/pledge\/browse\/extras\/subscribers-store"}}},
          "subscription": {"item":{"link":{"href":"\/pledge\/subscriptions"}}}
        },
        "layouts": {
          "store-all": null
        },
        "localeSelector": {
          "available": {
            "languages": ["en"]
          },
          "selected": {
            "language": "en"
          }
                ,"languages": {"en":{"code":"en","label":"English","codeLabel":"en","subLabel":null,"altCodes":null,"badges":[],"url":"\/en\/citizens\/Steinchen"}}
                      ,"currency": {"USD":{"iso":"USD","symbol":"$","label":"United States dollar"},"CAD":{"iso":"CAD","symbol":"$","label":"Canadian dollar"},"EUR":{"iso":"EUR","symbol":"\u20ac","label":"Euro"},"GBP":{"iso":"GBP","symbol":"\u00a3","label":"Pound sterling"}}
              },
            "tools": {
          "launcher-link": {
            "title": "Download",
            "href": "\/download"
          }
        },
        "translations": {
          "backToRSIMobile": "BACK TO RSI.com",
          "cancelButton": "Cancel",
          "confirmButton": "Confirm",
          "currencyTitle": "Currency",
          "languageTitle": "Language"
        }
      }'>
    </div>
    
    <div
        data-rsi-component="PlatformBar.Head"
        data-rsi-component-props='{
            "breadCrumbCurrentItem": null    }'
        data-orion-skin="default"
        data-orion-theme=""
    ></div>
    
      <div
        data-rsi-component="PlatformBar.Navigation"
        data-orion-skin="default"
        data-orion-theme=""
      ></div>
        
    
        <div id="bodyWrapper">
                <div id="platform-client-root"></div>
          
        
      <div class="page-wrapper">
        
        <div id="contentbody" class="public-profile public-profile-landing" style="">
          
      <div id="profile" class="wrapper">
        <h1 class="page-title ">
      <span class="top-line"></span>
      <span class="inner-line"></span>
      <span class="icon"></span>CITIZEN DOSSIER
      <span class="bottom-line"></span>
    </h1>    <div id="public-profile" class="account-profile">
              <div class="tabs tabs2">
            <div class="holder clearfix">
              <a href="/citizens/Steinchen" class="holotab active">
                <span class="text trans-02s">Overview</span>
                <span class="top trans-02s"></span>
                <span class="bottom trans-02s"></span>
              </a>
              <a href="/citizens/Steinchen/organizations" class="holotab right">
                <span class="text trans-02s">Organizations</span>
                <span class="top trans-02s"></span>
                <span class="bottom trans-02s"></span>
              </a>
            </div>
          </div>
          <div class="profile-content overview-content clearfix">
            <p class="entry citizen-record">
              <span class="label">UEE Citizen Record</span>
              <strong class="value">#128</strong>
            </p>
            <div class="box-content profile-wrapper clearfix">
              <div class="inner-bg clearfix">
                <div class="profile left-col">
                  <span class="title">Profile </span>
                  <div class="inner clearfix">
                    <div class="thumb">
                      <img src="/media/va66xhawk8k9mr/heap_infobox/D528d0f9e6560e707aecc9c1ae9d84ae.jpg" />
                      <span class="deco-corner top left"></span>
                      <span class="deco-corner top right"></span>
                      <span class="deco-corner bottom left"></span>
                      <span class="deco-corner bottom right"></span>
                    </div>
                    <div class="info">
                      <p class="entry">
                        <strong class="value">Steinchen</strong>
                      </p>
                      <p class="entry">
                        <span class="label">Handle name</span>
                        <strong class="value">Steinchen</strong>
                      </p>
                                          <p class="entry">
                                                  <span class="icon">
                              <img src="/media/o2k1asxgmail5r/heap_thumb/Spectrum_1M_24px.png"/>
                            </span>
                                                <span class="value">Aeon Club</span>
                        </p>
                                      </div>
                  </div>
                </div>
                <div class="main-org right-col visibility-V">
                  <span class="title">Main organization </span>
                  <div class="inner clearfix">
                                      <div class="thumb">
                                                                                      <a href="/orgs/C0IN"><img src="/media/ypl4xbzsw1t2yr/heap_infobox/C0IN-Logo.png" /></a>
                                            <span class="deco-corner top left"></span>
                        <span class="deco-corner top right"></span>
                        <span class="deco-corner bottom left"></span>
                        <span class="deco-corner bottom right"></span>
                      </div>
                      <div class="info">
                        <p class="entry">
                                                <a href="/orgs/C0IN" class="value data10" style="background-position:-297px center">Cooperative Industries</a>
                        </p>
                        <p class="entry">
                                                <span class="label data4">Spectrum Identification (SID)</span>
                                                <strong class="value data10">C0IN</strong>
                        </p>
                        <p class="entry">
                                                <span class="label data13">Organization rank</span>
                                                <strong class="value data11">Mitglied</strong>
                        </p>
                        <div class="ranking data10">
                                                                            <span class="active"><span></span></span>
                                                      <span ><span></span></span>
                                                      <span ><span></span></span>
                                                      <span ><span></span></span>
                                                      <span ><span></span></span>
                                                                      </div>
                      </div>
                                  </div>
                  <span class="deco-separator top"></span>
                  <span class="deco-separator bottom"></span>
                              </div>
              </div>
              <span class="deco-corner top left"></span>
              <span class="deco-corner top right"></span>
              <span class="deco-corner bottom left"></span>
              <span class="deco-corner bottom right"></span>
              <span class="deco-edge left"><span class="top"></span><span class="bottom"></span></span>
              <span class="deco-edge right"><span class="top"></span><span class="bottom"></span></span>
            </div>
            <div class="left-col">
              <div class="inner">
                <p class="entry">
                  <span class="label">Enlisted</span>
                  <strong class="value">Sep 10, 2012</strong>
                </p>
                              <p class="entry">
                    <span class="label">Location</span>
                    <strong class="value">
                      Austria
                                          , Steiermark
                                      </strong>
                  </p>
                            <p class="entry">
                  <span class="label">Fluency</span>
                  <strong class="value">                                                  English,                                  German                                </strong>
                </p>
              </div>
            </div>
            <div class="right-col">
              <div class="inner">
                                                                </div>
            </div>
                  </div>
        </div>
      </div>
    
        </div>
        
      </div>
    
      
    
    
    
                   <script id="tpl_number_counter_digits" type="text/x-jsmart-tmpl">{if !$seperator}{$seperator=','}{/if}
    {if !$first_max}{$first_max=9}{/if}
    {for $digit = 0 to $length-1}
      <div class="mask">
        <div class="carousel">
          {if $digit == 0}
            {$max = $first_max}
          {else}
            {$max = 9}
          {/if}
          {for $i=0 to $max}
            <div class="item {if $val_arr[$digit] == $i}on{/if}" rel="{$i}">{$i}</div>
          {/for}
        </div>
      </div>
      {if ($length - $digit) % 3 == 1 && $digit != $length-1}
      <div class="seperator">{$seperator}</div>
      {/if}
    {/for}</script>
    <script id="base_modal" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
      <div class="top-border">
        {block name="modal_lines"}
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        {/block}
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        {block name="modal_content"}{/block}
        {block name="modal_footer"}{/block}
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
        {block name="modal_lines"}
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        {/block}
      </div>
    </div></script>
    <script id="base_modal_flat" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
      
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        {block name="modal_content"}{/block}
        {block name="modal_footer"}{/block}
      </div>
      
    </div></script>
    <script id="tpl_modals_slideshow" type="text/x-jsmart-tmpl"><img class="top-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_top.png">
    <a href="" class="close js-close"></a>
    <div class="mask">
      <a class="js-prev prev control"></a>
      <a class="js-next next control"></a>
      <div class="slideshow-carousel carousel" rel="{$index}">
        {foreach from=$images item="image"}
          <div class="{if $index == $image@index}on{/if}">
          {if $image.is_video}
            <div class="video-holder">
              <div id="slideshow_video_{$image@index}" data-source="{$image->source_url}">
                <video width="100%" height="100%" preload="auto" {if $video}src="{$image->source_url}"{/if} controls></video>
              </div>
            </div>
          {else}
            <div class="media js-media-slideshow-{$image@iteration}">
            {if $image.low_res}
              <picture>
                <!--[if IE 9]><video style="display: none;"><![endif]-->
                <source data-srcset="{$image.full_res}" media="(min-width: 300px)" />
                <!--[if IE 9]></video><![endif]-->
                <img data-srcset="{$image.low_res}" alt="{$image.title}" />
              </picture>
            {else}
              <img data-src="{$image.source_url}" />
            {/if}
            </div>
          {/if}
            <div class="text">
              {if !$image.is_video}
              <a href="{$image.source_url}" class="download"></a>
              {/if}
              <div class="copyright">© 2012-{$year}<br />Cloud Imperium Games Corporation &<br />Roberts Space Industries Corp.</div>
              <div class="page-number">{$image@iteration} / {count($images)}</div>
              <div class="caption v-center">{if $image.title && $image.title != "undefined"}{$image.title}{/if}</div>
              <div class="cboth"></div>
            </div>
          </div>
        {/foreach}
      </div>
    </div>
    <img class="bottom-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_bottom.png"></script>
    <script id="tpl_contact_us" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
      <div class="top-border">
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        
    <div id="contact" class="inner-content on">
      <h2><span class="icon"></span>CONTACT</h2>
      <div class="padder">
        <div class="separator"></div>
        <form name="" action="" method="POST" class="legacy-form">
      <div class="error-message js-error-message"></div>
      <div class="success-message js-success-message"></div>
        <fieldset>
        <label for="contact_subject">Subject</label>
        <input type="text" name="subject" value="" class="trans-02s trans-color trans-box-shadow" id="contact_subject" />
        <label>Contacting us for:</label>
        <ul class="category-info">
                <li id="tech_support_info">Questions about download, installation, networking, or in-game client problems</li>
                <li id="subscription_info">Questions about monthly and yearly subscription plans</li>
                <li id="account_billing_info">Issues related to your account, such as incorrect information or ability to access account, or Billing with regards to payments and payment methods</li>
                <li id="melt_request_info">To reclaim a pledge over $1,000 for store credit (please note - this is a permanent action)</li>
                <li id="merchandise_info">Questions about physical and/or shipped merchandise</li>
                <li id="hacked_info">Issues related to compromised account or missing pledge.</li>
                <li id="account_recovery_info">For issues with account authentication, lost passwords and related queries</li>
                <li id="probation_info">Issues related to forums probation or ban</li>
                <li id="refund_request_info">Refund requests and related inquiries</li>
                <li id="customer_support_info">For general questions and queries regarding Star Citizen</li>
              </ul>
      </fieldset>
      <fieldset>
        <label for="contact_text">Description</label>
        <textarea name="text" class="trans-02s trans-color trans-box-shadow" id="contact_text"></textarea>
      </fieldset>
      <div class="contact-submit-wrapper">
        <div class="line"></div>
        <button class="submit js-submit"><strong>submit your message</strong></button>
      </div>
    </form>
        <div class="separator"></div>
      </div>
    </div>
    
        
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
      </div>
    </div></script>
    <script id="tpl_error" type="text/x-jsmart-tmpl"><div class="modal-error js-modal-error">
      <p class="modal-text js-modal-text"></p>
      <a class="close js-close trans-03s .trans-opacity" href=""></a>
    </div></script>
    <script id="tpl_success" type="text/x-jsmart-tmpl"><div class="modal-success js-modal-success">
      <p class="modal-text js-modal-text"></p>
      <a class="close js-close trans-03s .trans-opacity" href=""></a>
    </div></script>
    <script id="tpl_progress" type="text/x-jsmart-tmpl"><div class="modal-progress js-modal-progress">
      <div class="traj-loader">
        <div class="fast-blink"></div>
        <span class="modal-text js-modal-text"></span>
      </div>
    </div></script>
    <script id="tpl_outbound" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
      <div class="top-border">
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        
    <div id="outbound" class="inner-content on">
      <h2><span class="icon"></span>OUTBOUND LINK</h2>
      <div class="padder">
        <div class="separator"></div>
        <form name="" action="" method="POST" class="legacy-form">
          <div class="error-message js-error-message"> <span class=important>WARNING</span><br/><br/> This link will bring you outside of the RSI site and into the depths of the internet. Continue?<br/><br/><span class="url"></span> </div>
          <div class="success-message js-success-message"><span class=important>STAND BY</span><br/><br/> Initiating hyperlink.<br/><br/></div>
    
          <fieldset class="clearfix last">
            <span class="submit-wrapper">
              <span class="submit-hover trans-02s trans-opacity"></span>
              <input type="submit" value="WARP" class="trans-02s trans-color trans-background" />
            </span>
          </fieldset>
        </form>
        <div class="separator"></div>
      </div>
    </div>
    
        
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
      </div>
    </div></script>
    
    <script id="tpl_l-notification-bar" type="text/x-jsmart-tmpl"><div class="l-notification-bar js-notification-bar">
    
      <div class="l-notification-bar__watermark js-svg-inliner h-svg__logo-star-citizen"></div>
    
      <div class="l-notification-bar__boxes">
        {if !$viewedCookieNotif}
          <div class="l-notification-bar__box">
            {include file='tpl_c-notification'
              type='cookie'
              title='COOKIES:'
              message="Our website uses Google Analytics to analyze our traffic. <br/>To learn how you can control Google's use of your data and how you can opt out <a href='https://www.google.com/policies/privacy/partners/'>click here</a>."
              linkText='See Details'
              buttonText='Got it!'}
          </div>
        {/if}
    
        {if !$viewedPrivacyNotif}
          <div class="l-notification-bar__box">
            {include file='tpl_c-notification'
              type='privacy'
              title='PRIVACY POLICY:'
              message='We adjusted the PP to reflect the decision of the European Court of Justice regarding Safe Harbor, the fact that RSI has moved and added some services providers.'
              linkText='View Privacy Policy'
              buttonText='Got it!'}
          </div>
        {/if}
      </div>
    
    </div>
    </script>
    <script id="tpl_c-notification" type="text/x-jsmart-tmpl"><div class="c-notification js-bottom-notif-msg-{$type}">
        <div class="c-notification__title">{$title}</div>
        <div class="c-notification__message">
          {$message}
        </div>
    
        {if $linkText}
            <div class="c-notification__wrapper-link">
                <a class="c-notification__link js-bottom-notif-link-{$type}">
                {$linkText}
                </a>
            </div>
        {/if}
    
        <a class="c-notification__button js-bottom-notif-btn-{$type}">
    
          <span class="c-notification__button-text">
           {$buttonText}
          </span>
    
          {if $type neq 'announcement'}
            <div class="c-iconed__icon c-iconed__icon--checkmark"></div>
          {/if}
        </a>
    </div>
    </script>
    
    <script id="tpl_confirm" type="text/x-jsmart-tmpl"><div class="modal-confirm js-modal-confirm clearfix">
      <p class="modal-text js-modal-text"></p>
      <a class="bt-close js-close trans-03s trans-opacity" href=""></a>
      <a class="bt-confirm js-confirm trans-03s trans-opacity" href=""></a>
        <div class="buttons">
            <a class="shadow-button trans-02s trans-color js-close bt-close rm"     >
      <span class="label js-label trans-02s">Cancel</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
            <a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
      <span class="label js-label trans-02s">Confirm</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
        </div>
    </div>
    </script>
    <script id="tpl_alert" type="text/x-jsmart-tmpl"><div class="modal-alert js-modal-alert clearfix">
      <p class="modal-text js-modal-text"></p>
      <div class="buttons">
        <a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
      <span class="label js-label trans-02s">OK</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
      </div>
    </div></script>
    <script id="tpl_video" type="text/x-jsmart-tmpl">{extends file="base_modal"}
    {block name='modal_content'}
    <div id="ship-commercial" class="inner-content">
    
      <div class="hr"></div>
      <div class="content-block4">
    
        <div class="bottom"></div>
      </div>
      {if $distant_source=="vimeo"}
      <iframe id="commercial" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="//player.vimeo.com/video/{$video_id}?wmode=transparent" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>
      {else}
      <iframe id="commercial" frameborder="0" allowfullscreen="1" title="YouTube video player" width="100%" height="100%" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="https://www.youtube.com/embed/{$video_id}?autoplay=1"></iframe>
      {/if}
    </div>
    {/block}
    </script>
          
    
          
            
        
    
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KHNFZPT"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->
    
    
    <div data-rsi-component="PlatformFooter" data-rsi-component-props='{
      "currentSection": "rsi",
      "wscAbout": "/star-citizen",
      "wscPlay": "/playstarcitizen",
      "s42Game": "/squadron42",
      "s42Enlist": "/squadron42#enlist",
      "rsiCommlink": "/comm-link",
      "rsiCommunity": "/community-hub",
      "rsiRoadmap": "/roadmap",
      "showStoreMenu": "1",
      "isStoreMenuActive": "",
      "rsiStore": "/pledge",
      "rsiDownload": "/download",
      "isLauncherMenuActive": "",
      "rsiSpectrum": "/spectrum/community/SC",
      "showCitizenconMenu": "1",
      "rsiCitizencon": "/citizencon",
      "utilitiesHelp": "//support.robertsspaceindustries.com",
      "utilitiesPress": "/press",
      "utilitiesCareers": "https://cloudimperiumgames.com/join-us",
      "utilitiesAcknowledgement": "/acknowledgements",
      "utilitiesRedeemCode": "/pledge/redeem-code",
      "legalLegal": "/legal",
      "legalTos": "/tos",
      "legalPrivacy": "/privacy",
      "legalEula": "/eula",
      "legalDmca": "/dmca",
      "legalDisclosure": "/responsible-disclosure",
      "legalCaliforniaLegalNoticeAtCollection": "/privacy#california",
      "legalCaliforniaLegalPersonalInformation": "/cookies#preferences",
      "isConsentRequired": "",
      "clientRecordCountry": "GB",
      "cigLink": "https://cloudimperiumgames.com",
      "displayStarEngine": ""
    }'></div>
          
        </div>
      </body>
    </html>

    """

@pytest.fixture
def npc_profile():
    return """
    <!DOCTYPE html>
        
    <html lang="en">
      <head>
            
        <script
        id="TagManager"
        data-cookieconsent="ignore"
        data-app-name="rsi-heap"
        data-app-version="9.177.0"
        data-category="site"
        data-sub-category="missing"
        src="/tag-manager/script.js"
        type="text/javascript"></script>
            <script
        type="text/javascript"
        id="Cookiebot"
        src="https://consent.cookiebot.com/uc.js"
        data-cbid="a687ee30-df65-45a0-9d22-90de6c1bb964"
        data-blockingmode="auto"
        data-georegions="{'region':'US-06,US-51,AT,BE,BG,HR,CY,CZ,DK,EE,FI,FR,DE,GR,HU,IE,IT,LV,LT,LU,MT,NL,PL,PT,RO,SK,SL,ES,SE','cbid':'a687ee30-df65-45a0-9d22-90de6c1bb964'}"></script>
        <script id="CookieConsent" src="/cookie-consent/script.js?async=false" type="text/javascript"></script>
      <link href="/rsi/static/css/cookiebot.css?v=9.177.0" rel="stylesheet" />
            <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    
        <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
        <meta name="description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans.">
    
        <meta name="csrf-token" content="9de548adfd3c7270d237683ea4ea2b174d51689a95e7352bb2325fd5bdabc7df" />
        <meta property="og:site_name" content="
      404 - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
    " />
        <meta property="og:image" content="https://cdn.robertsspaceindustries.com/static/images/RSI-fb.jpg" />
        <meta property="og:description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans." />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://robertsspaceindustries.com/en/citizens/Quasigrazer_Boreal_2979717832657" />
        <meta property="og:locale" content="en" />
    
        <title>
      404 - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
    </title>
    
        <link rel="canonical" href="https://robertsspaceindustries.com/en/citizens/Quasigrazer_Boreal_2979717832657">
    
        
                      <link rel="alternate" href="https://robertsspaceindustries.com/en/citizens/Quasigrazer_Boreal_2979717832657" hreflang="en">
                                
    
            <link rel=preconnect href="//sentry.turbulent.ca">
        <link rel=preconnect href="//gstatic.com">
        <link rel=preconnect href="//www.recaptcha.net">
        <link rel=preconnect href="//www.googletagmanager.com">
          
    
            <link href="/rsi/static/css/rsi-minimal.css?v=9.177.0" media="all" rel="stylesheet">
        
    <link href="/rsi/static/css/cross-brand-less.css?v=9.177.0" media="all" rel="stylesheet">
    
    
              
    <script type="text/javascript" src="/cache/en/rsi-external-js.js?v=9.177.0"></script>
    <script type="text/javascript" src="/cache/en/rsi-templates-js.js?v=9.177.0"></script>
    
            
              
    <link rel="stylesheet" href="https://use.typekit.net/dhw3beb.css">
    
    
    
              
    <script type="text/javascript" src='/rsi/static/packages/core/rsi.core.build.e8130.js'></script>
    <script type="text/javascript" src='/rsi/static/packages/account/rsi.account.build.74772.js'></script>
    <script type="text/javascript" src='/rsi/static/packages/store/rsi.store.build.0278b.js'></script>
    
    <script>
                    
        $(document).ready(function() {
        window.Common = new RSI.Common({});
        window.Main = new RSI.Main({
            'is_mobile': 0,
            'probation_cookie' : '',
            'require_captcha': 0
        });
        window.Mark = new Turbulent.Mark({ 'name' : 'Rsi-XSRF', 'token' : 'wJsPaA:eY5HymRMrFxl6xOjU/Ef/g', 'ttl' : 1800 });
    
        window.WscOverlay = new RSI.WscOverlay({});
    
        var destinations = [];
    
    window.Main.destinations = destinations;    
        
        
        });
    
        $(window).load(function() {
        
        });
    </script>
    
    
        <script>
        window.recaptcha_is_loaded = false;
        window.on_recaptcha_load_callback = function() {
        window.recaptcha_is_loaded = true;
        };
    </script>
    
    <script
        src="https://www.recaptcha.net/recaptcha/enterprise.js?onload=on_recaptcha_load_callback&render=6LerBOgUAAAAAKPg6vsAFPTN66Woz-jBClxdQU-o"
        async defer>
    </script>
        <script type="text/javascript">
          
        </script>
    
        
        
      <style>
        
          background:url(https://cdn.robertsspaceindustries.com/static/images/noisebg.gif) repeat center top #000b11;
        
      </style>
    
        <link href="https://robertsspaceindustries.com/rsi/assets/fonts.css?family=Electrolize|Orbitron:400,500,700|Quantico|Share+Tech+Mono" rel="stylesheet" type="text/css">
    
        <link href="/cache/en/rsi-css.css?v=9.177.0" media="all" rel="stylesheet">
    
    
        <script 
        type="module" 
        data-cookieconsent="ignore" 
        src="https://robertsspaceindustries.com/plt-client/plt-client.es.js"
        data-platform-client-props="{&quot;lang&quot;:&quot;en&quot;,&quot;user&quot;:{&quot;isSignedIn&quot;:true,&quot;avatar&quot;:&quot;\/media\/0rixm629l5bwwr\/avatar\/A5ce2752-Ce33-446e-Ae18-2dab9f9ead8a.jpg&quot;,&quot;referral&quot;:{&quot;referralCode&quot;:&quot;STAR-73KP-54LB&quot;,&quot;referralUrl&quot;:&quot;https%3A%2F%2Frobertsspaceindustries.com%2Fenlist%3Freferral%3DSTAR-73KP-54LB&quot;,&quot;referralUrlCopy&quot;:&quot;https:\/\/robertsspaceindustries.com\/enlist?referral=STAR-73KP-54LB&quot;},&quot;useLegacyAccountPanel&quot;:false,&quot;isSubscriber&quot;:false,&quot;favorite&quot;:{&quot;img&quot;:&quot;https:\/\/media.robertsspaceindustries.com\/9qvh53v4nyx8d\/heap_note.png&quot;,&quot;name&quot;:&quot;Civilian&quot;},&quot;xsrfToken&quot;:{&quot;cookieName&quot;:&quot;Rsi-XSRF&quot;,&quot;token&quot;:&quot;wJsPaA:eY5HymRMrFxl6xOjU\/Ef\/g&quot;,&quot;ttlMargin&quot;:1800000,&quot;cookieValue&quot;:null}}}"
    ></script>
      </head>
    
        <body id="missing" class=""  lang=en localized=1>
        
          <div
      data-rsi-component="Platform.Notification"
      data-rsi-component-props='{
        "id":"145",
        "type": "announcement",
        "severity": "P",
        "title":"Fly For Free",
        "content":"Play Star Citizen for FREE until April 28 and test fly 6 legendary ships!",
        "url":"https://robertsspaceindustries.com/en/flyfree"
      }'
    ></div>
        
    
        
                
    <div 
      data-rsi-component="PlatformBar.Data"
      data-rsi-component-props='{
        "root": "home",
        "active": "dyn_bd_first_level_Quasigrazer_Boreal_2979717832657",
        "api": {
          "nav": {
            "url": "/nav/",
            "load": ["main","games","shop","explore","community","support","tools"]
          }
        },
        "nodes": {
                      "dyn_bd_first_level_Quasigrazer_Boreal_2979717832657": {"slug":"dyn_bd_first_level_Quasigrazer_Boreal_2979717832657","parent":"home","item":{"title":"Quasigrazer_Boreal_2979717832657"}},
                      "home": {
            "toolbar": ["launcher-link"]
          },
                "buy-star-citizen": {
            "item": {
              "link": {
                "href": "\/download"
              }
            }
          },
          "subscribers": {"children":["subscription-become","subscribers-store"]},
          "subscribers-store": {"item":{"link":{"href":"\/store\/pledge\/browse\/extras\/subscribers-store"}}},
          "subscription": {"item":{"link":{"href":"\/pledge\/subscriptions"}}}
        },
        "layouts": {
          "store-all": null
        },
        "localeSelector": {
          "available": {
            "languages": ["en"]
          },
          "selected": {
            "language": "en"
          }
                ,"languages": {"en":{"code":"en","label":"English","codeLabel":"en","subLabel":null,"altCodes":null,"badges":[],"url":"\/en\/citizens\/Quasigrazer_Boreal_2979717832657"}}
                      ,"currency": {"USD":{"iso":"USD","symbol":"$","label":"United States dollar"},"CAD":{"iso":"CAD","symbol":"$","label":"Canadian dollar"},"EUR":{"iso":"EUR","symbol":"\u20ac","label":"Euro"},"GBP":{"iso":"GBP","symbol":"\u00a3","label":"Pound sterling"}}
              },
            "tools": {
          "launcher-link": {
            "title": "Download",
            "href": "\/download"
          }
        },
        "translations": {
          "backToRSIMobile": "BACK TO RSI.com",
          "cancelButton": "Cancel",
          "confirmButton": "Confirm",
          "currencyTitle": "Currency",
          "languageTitle": "Language"
        }
      }'>
    </div>
    
    <div
        data-rsi-component="PlatformBar.Head"
        data-rsi-component-props='{
            "breadCrumbCurrentItem": null    }'
        data-orion-skin="default"
        data-orion-theme=""
    ></div>
    
      <div
        data-rsi-component="PlatformBar.Navigation"
        data-orion-skin="default"
        data-orion-theme=""
      ></div>
        
    
        <div id="bodyWrapper">
                <div id="platform-client-root"></div>
          
        
      <div class="page-wrapper">
        
        <div id="contentbody" class="" style="">
          
    
    <div class="content-wrapper clearfix">
      <div class="wrapper">
      
        <div class="circle-wrapper">
          <div class="circle"></div>
          <div class="octo-big fadeIn fade-four"></div>
          <div class="octo-small fadeIn fade-four"></div>
          
          <div class="compass fadeIn fade-one">
            <div class="glow fadeIn fade-three"></div>
            <div class="thin-line"></div>
            <div class="large-line fadeIn fade-three"></div>
            <div class="arrow fadeIn fade-three"></div>          
          </div>
        </div>
        <div class="elem-wrapper">
          <div class="text">
            <div class="status fadeIn fade-one">POSITION STATUS CODE:</div>
            <div class="code fadeIn fade-two">
              <span class="num fadeIn fade-three">404</span>
              <span class="desc fadeIn fade-three">NAVIGATING UNCHARTED TERRITORY</span>
            </div>
            <div class="inner-text fadeIn fade-four">
              <p><strong>Warning:</strong></p>
              <p>You are currently venturing unknown space. In the event you are lost, the UEE highly recommends plotting a new destination back towards home-space.</p>
              <a class="animbtn backbtn trans-03s trans-color right" href="/" id="backtohome">
                  <span class="backarrow abs-overlay">
                    <span class="arrowline abs-overlay trans-03s">
                      <span class="arrowhead abs-overlay"></span>
                    </span>
                  </span>
                  <span class="backslant abs-overlay trans-03s"></span>
                  <span class="cut abs-overlay"></span>
                  <span class="bullet abs-overlay">
                    <span class="abs-overlay trans-03s trans-opacity"></span>
                  </span>
                  PLOT NEW COURSE
              </a>
            </div>
          </div>
          
          <div class="current-traj fadeIn">
            <div class="icon"></div>
            CURRENT TRAJECTORY
          </div>
          <div class="prev-traj fadeIn fade-four">
            <div class="icon"></div>
            PREVIOUS TRAJECTORY
            <span>-3.57 DAY</span>
          </div>
          
          <div class="traj-info fadeIn fade-three">
            <div class="info fadeIn fade-four">
              <div class="icon"></div>
              <strong>STATUS:</strong><br />
              ON COURSE
              <span></span>
            </div>
            <div class="info fadeIn fade-four-two">
              <div class="icon"></div>
              <strong>PATH DEVIATION:</strong><br />
              -0.00021
              <span></span>
            </div>
            <div class="info fadeIn fade-four-three">
              <div class="icon"></div>
              <strong>PREDICTED DEVIATION:</strong><br />
              -0.00015
              <span></span>
            </div>
            <div class="line"></div>
          </div>
        </div>
        
      </div>
    
    </div>
    
    
        </div>
        
      </div>
    
      
    
    
    
                   <script id="tpl_number_counter_digits" type="text/x-jsmart-tmpl">{if !$seperator}{$seperator=','}{/if}
    {if !$first_max}{$first_max=9}{/if}
    {for $digit = 0 to $length-1}
      <div class="mask">
        <div class="carousel">
          {if $digit == 0}
            {$max = $first_max}
          {else}
            {$max = 9}
          {/if}
          {for $i=0 to $max}
            <div class="item {if $val_arr[$digit] == $i}on{/if}" rel="{$i}">{$i}</div>
          {/for}
        </div>
      </div>
      {if ($length - $digit) % 3 == 1 && $digit != $length-1}
      <div class="seperator">{$seperator}</div>
      {/if}
    {/for}</script>
    <script id="base_modal" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
      <div class="top-border">
        {block name="modal_lines"}
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        {/block}
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        {block name="modal_content"}{/block}
        {block name="modal_footer"}{/block}
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
        {block name="modal_lines"}
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        {/block}
      </div>
    </div></script>
    <script id="base_modal_flat" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
      
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        {block name="modal_content"}{/block}
        {block name="modal_footer"}{/block}
      </div>
      
    </div></script>
    <script id="tpl_modals_slideshow" type="text/x-jsmart-tmpl"><img class="top-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_top.png">
    <a href="" class="close js-close"></a>
    <div class="mask">
      <a class="js-prev prev control"></a>
      <a class="js-next next control"></a>
      <div class="slideshow-carousel carousel" rel="{$index}">
        {foreach from=$images item="image"}
          <div class="{if $index == $image@index}on{/if}">
          {if $image.is_video}
            <div class="video-holder">
              <div id="slideshow_video_{$image@index}" data-source="{$image->source_url}">
                <video width="100%" height="100%" preload="auto" {if $video}src="{$image->source_url}"{/if} controls></video>
              </div>
            </div>
          {else}
            <div class="media js-media-slideshow-{$image@iteration}">
            {if $image.low_res}
              <picture>
                <!--[if IE 9]><video style="display: none;"><![endif]-->
                <source data-srcset="{$image.full_res}" media="(min-width: 300px)" />
                <!--[if IE 9]></video><![endif]-->
                <img data-srcset="{$image.low_res}" alt="{$image.title}" />
              </picture>
            {else}
              <img data-src="{$image.source_url}" />
            {/if}
            </div>
          {/if}
            <div class="text">
              {if !$image.is_video}
              <a href="{$image.source_url}" class="download"></a>
              {/if}
              <div class="copyright">© 2012-{$year}<br />Cloud Imperium Games Corporation &<br />Roberts Space Industries Corp.</div>
              <div class="page-number">{$image@iteration} / {count($images)}</div>
              <div class="caption v-center">{if $image.title && $image.title != "undefined"}{$image.title}{/if}</div>
              <div class="cboth"></div>
            </div>
          </div>
        {/foreach}
      </div>
    </div>
    <img class="bottom-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_bottom.png"></script>
    <script id="tpl_contact_us" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
      <div class="top-border">
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        
    <div id="contact" class="inner-content on">
      <h2><span class="icon"></span>CONTACT</h2>
      <div class="padder">
        <div class="separator"></div>
        <form name="" action="" method="POST" class="legacy-form">
      <div class="error-message js-error-message"></div>
      <div class="success-message js-success-message"></div>
        <fieldset>
        <label for="contact_subject">Subject</label>
        <input type="text" name="subject" value="" class="trans-02s trans-color trans-box-shadow" id="contact_subject" />
        <label>Contacting us for:</label>
        <ul class="category-info">
                <li id="tech_support_info">Questions about download, installation, networking, or in-game client problems</li>
                <li id="subscription_info">Questions about monthly and yearly subscription plans</li>
                <li id="account_billing_info">Issues related to your account, such as incorrect information or ability to access account, or Billing with regards to payments and payment methods</li>
                <li id="melt_request_info">To reclaim a pledge over $1,000 for store credit (please note - this is a permanent action)</li>
                <li id="merchandise_info">Questions about physical and/or shipped merchandise</li>
                <li id="hacked_info">Issues related to compromised account or missing pledge.</li>
                <li id="account_recovery_info">For issues with account authentication, lost passwords and related queries</li>
                <li id="probation_info">Issues related to forums probation or ban</li>
                <li id="refund_request_info">Refund requests and related inquiries</li>
                <li id="customer_support_info">For general questions and queries regarding Star Citizen</li>
              </ul>
      </fieldset>
      <fieldset>
        <label for="contact_text">Description</label>
        <textarea name="text" class="trans-02s trans-color trans-box-shadow" id="contact_text"></textarea>
      </fieldset>
      <div class="contact-submit-wrapper">
        <div class="line"></div>
        <button class="submit js-submit"><strong>submit your message</strong></button>
      </div>
    </form>
        <div class="separator"></div>
      </div>
    </div>
    
        
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
      </div>
    </div></script>
    <script id="tpl_error" type="text/x-jsmart-tmpl"><div class="modal-error js-modal-error">
      <p class="modal-text js-modal-text"></p>
      <a class="close js-close trans-03s .trans-opacity" href=""></a>
    </div></script>
    <script id="tpl_success" type="text/x-jsmart-tmpl"><div class="modal-success js-modal-success">
      <p class="modal-text js-modal-text"></p>
      <a class="close js-close trans-03s .trans-opacity" href=""></a>
    </div></script>
    <script id="tpl_progress" type="text/x-jsmart-tmpl"><div class="modal-progress js-modal-progress">
      <div class="traj-loader">
        <div class="fast-blink"></div>
        <span class="modal-text js-modal-text"></span>
      </div>
    </div></script>
    <script id="tpl_outbound" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
      <div class="top-border">
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        
    <div id="outbound" class="inner-content on">
      <h2><span class="icon"></span>OUTBOUND LINK</h2>
      <div class="padder">
        <div class="separator"></div>
        <form name="" action="" method="POST" class="legacy-form">
          <div class="error-message js-error-message"> <span class=important>WARNING</span><br/><br/> This link will bring you outside of the RSI site and into the depths of the internet. Continue?<br/><br/><span class="url"></span> </div>
          <div class="success-message js-success-message"><span class=important>STAND BY</span><br/><br/> Initiating hyperlink.<br/><br/></div>
    
          <fieldset class="clearfix last">
            <span class="submit-wrapper">
              <span class="submit-hover trans-02s trans-opacity"></span>
              <input type="submit" value="WARP" class="trans-02s trans-color trans-background" />
            </span>
          </fieldset>
        </form>
        <div class="separator"></div>
      </div>
    </div>
    
        
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
      </div>
    </div></script>
    
    <script id="tpl_l-notification-bar" type="text/x-jsmart-tmpl"><div class="l-notification-bar js-notification-bar">
    
      <div class="l-notification-bar__watermark js-svg-inliner h-svg__logo-star-citizen"></div>
    
      <div class="l-notification-bar__boxes">
        {if !$viewedCookieNotif}
          <div class="l-notification-bar__box">
            {include file='tpl_c-notification'
              type='cookie'
              title='COOKIES:'
              message="Our website uses Google Analytics to analyze our traffic. <br/>To learn how you can control Google's use of your data and how you can opt out <a href='https://www.google.com/policies/privacy/partners/'>click here</a>."
              linkText='See Details'
              buttonText='Got it!'}
          </div>
        {/if}
    
        {if !$viewedPrivacyNotif}
          <div class="l-notification-bar__box">
            {include file='tpl_c-notification'
              type='privacy'
              title='PRIVACY POLICY:'
              message='We adjusted the PP to reflect the decision of the European Court of Justice regarding Safe Harbor, the fact that RSI has moved and added some services providers.'
              linkText='View Privacy Policy'
              buttonText='Got it!'}
          </div>
        {/if}
      </div>
    
    </div>
    </script>
    <script id="tpl_c-notification" type="text/x-jsmart-tmpl"><div class="c-notification js-bottom-notif-msg-{$type}">
        <div class="c-notification__title">{$title}</div>
        <div class="c-notification__message">
          {$message}
        </div>
    
        {if $linkText}
            <div class="c-notification__wrapper-link">
                <a class="c-notification__link js-bottom-notif-link-{$type}">
                {$linkText}
                </a>
            </div>
        {/if}
    
        <a class="c-notification__button js-bottom-notif-btn-{$type}">
    
          <span class="c-notification__button-text">
           {$buttonText}
          </span>
    
          {if $type neq 'announcement'}
            <div class="c-iconed__icon c-iconed__icon--checkmark"></div>
          {/if}
        </a>
    </div>
    </script>
    
    <script id="tpl_confirm" type="text/x-jsmart-tmpl"><div class="modal-confirm js-modal-confirm clearfix">
      <p class="modal-text js-modal-text"></p>
      <a class="bt-close js-close trans-03s trans-opacity" href=""></a>
      <a class="bt-confirm js-confirm trans-03s trans-opacity" href=""></a>
        <div class="buttons">
            <a class="shadow-button trans-02s trans-color js-close bt-close rm"     >
      <span class="label js-label trans-02s">Cancel</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
            <a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
      <span class="label js-label trans-02s">Confirm</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
        </div>
    </div>
    </script>
    <script id="tpl_alert" type="text/x-jsmart-tmpl"><div class="modal-alert js-modal-alert clearfix">
      <p class="modal-text js-modal-text"></p>
      <div class="buttons">
        <a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
      <span class="label js-label trans-02s">OK</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
      </div>
    </div></script>
    <script id="tpl_video" type="text/x-jsmart-tmpl">{extends file="base_modal"}
    {block name='modal_content'}
    <div id="ship-commercial" class="inner-content">
    
      <div class="hr"></div>
      <div class="content-block4">
    
        <div class="bottom"></div>
      </div>
      {if $distant_source=="vimeo"}
      <iframe id="commercial" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="//player.vimeo.com/video/{$video_id}?wmode=transparent" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>
      {else}
      <iframe id="commercial" frameborder="0" allowfullscreen="1" title="YouTube video player" width="100%" height="100%" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="https://www.youtube.com/embed/{$video_id}?autoplay=1"></iframe>
      {/if}
    </div>
    {/block}
    </script>
          
    
          
            
        
    
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KHNFZPT"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->
    
    
    <div data-rsi-component="PlatformFooter" data-rsi-component-props='{
      "currentSection": "rsi",
      "wscAbout": "/star-citizen",
      "wscPlay": "/playstarcitizen",
      "s42Game": "/squadron42",
      "s42Enlist": "/squadron42#enlist",
      "rsiCommlink": "/comm-link",
      "rsiCommunity": "/community-hub",
      "rsiRoadmap": "/roadmap",
      "showStoreMenu": "1",
      "isStoreMenuActive": "",
      "rsiStore": "/pledge",
      "rsiDownload": "/download",
      "isLauncherMenuActive": "",
      "rsiSpectrum": "/spectrum/community/SC",
      "showCitizenconMenu": "1",
      "rsiCitizencon": "/citizencon",
      "utilitiesHelp": "//support.robertsspaceindustries.com",
      "utilitiesPress": "/press",
      "utilitiesCareers": "https://cloudimperiumgames.com/join-us",
      "utilitiesAcknowledgement": "/acknowledgements",
      "utilitiesRedeemCode": "/pledge/redeem-code",
      "legalLegal": "/legal",
      "legalTos": "/tos",
      "legalPrivacy": "/privacy",
      "legalEula": "/eula",
      "legalDmca": "/dmca",
      "legalDisclosure": "/responsible-disclosure",
      "legalCaliforniaLegalNoticeAtCollection": "/privacy#california",
      "legalCaliforniaLegalPersonalInformation": "/cookies#preferences",
      "isConsentRequired": "",
      "clientRecordCountry": "GB",
      "cigLink": "https://cloudimperiumgames.com",
      "displayStarEngine": ""
    }'></div>
          
        </div>
      </body>
    </html>

    """

@pytest.fixture
def pilot_nanoart_with_corp():

    return """
    <!DOCTYPE html>
        
    <html lang="en">
      <head>
            
        <script
        id="TagManager"
        data-cookieconsent="ignore"
        data-app-name="rsi-heap"
        data-app-version="9.178.2"
        data-category="account"
        data-sub-category="account-profile-public"
        src="/tag-manager/script.js"
        type="text/javascript"></script>
            <script
        type="text/javascript"
        id="Cookiebot"
        src="https://consent.cookiebot.com/uc.js"
        data-cbid="a687ee30-df65-45a0-9d22-90de6c1bb964"
        data-blockingmode="auto"
        data-georegions="{'region':'US-06,US-51,AT,BE,BG,HR,CY,CZ,DK,EE,FI,FR,DE,GR,HU,IE,IT,LV,LT,LU,MT,NL,PL,PT,RO,SK,SL,ES,SE','cbid':'a687ee30-df65-45a0-9d22-90de6c1bb964'}"></script>
        <script id="CookieConsent" src="/cookie-consent/script.js?async=false" type="text/javascript"></script>
      <link href="/rsi/static/css/cookiebot.css?v=9.178.2" rel="stylesheet" />
            <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    
        <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
        <meta name="description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans.">
    
        <meta name="csrf-token" content="9de548adfd3c7270d237683ea4ea2b174d51689a95e7352bb2325fd5bdabc7df" />
        <meta property="og:site_name" content="
    Nanoart | IDS-Nanoart - Invicta Corporation | IDSCORP (Expert) - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
    " />
        <meta property="og:image" content="https://cdn.robertsspaceindustries.com/static/images/RSI-fb.jpg" />
        <meta property="og:description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans." />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://robertsspaceindustries.com/en/citizens/IDS-Nanoart" />
        <meta property="og:locale" content="en" />
    
        <title>
    Nanoart | IDS-Nanoart - Invicta Corporation | IDSCORP (Expert) - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
    </title>
    
        <link rel="canonical" href="https://robertsspaceindustries.com/en/citizens/IDS-Nanoart">
    
        
                      <link rel="alternate" href="https://robertsspaceindustries.com/en/citizens/IDS-Nanoart" hreflang="en">
                                
    
            <link rel=preconnect href="//sentry.turbulent.ca">
        <link rel=preconnect href="//gstatic.com">
        <link rel=preconnect href="//www.recaptcha.net">
        <link rel=preconnect href="//www.googletagmanager.com">
          
    
            <link href="/rsi/static/css/rsi-minimal.css?v=9.178.2" media="all" rel="stylesheet">
        
    <link href="/rsi/static/css/cross-brand-less.css?v=9.178.2" media="all" rel="stylesheet">
    
    
              
    <script type="text/javascript" src="/cache/en/rsi-external-js.js?v=9.178.2"></script>
    <script type="text/javascript" src="/cache/en/rsi-templates-js.js?v=9.178.2"></script>
    
            
              
    <link rel="stylesheet" href="https://use.typekit.net/dhw3beb.css">
    
    
    
              
    <script type="text/javascript" src='/rsi/static/packages/core/rsi.core.build.e8130.js'></script>
    <script type="text/javascript" src='/rsi/static/packages/account/rsi.account.build.74772.js'></script>
    <script type="text/javascript" src='/rsi/static/packages/store/rsi.store.build.0278b.js'></script>
    
    <script>
                    
        $(document).ready(function() {
        window.Common = new RSI.Common({});
        window.Main = new RSI.Main({
            'is_mobile': 0,
            'probation_cookie' : '',
            'require_captcha': 0
        });
        window.Mark = new Turbulent.Mark({ 'name' : 'Rsi-XSRF', 'token' : 'edgQaA:fWuAImMepmSWIV6C9a4riA', 'ttl' : 1800 });
    
        window.WscOverlay = new RSI.WscOverlay({});
    
        var destinations = [];
    
    window.Main.destinations = destinations;    
        
        
        });
    
        $(window).load(function() {
        
        });
    </script>
    
    
        <script>
        window.recaptcha_is_loaded = false;
        window.on_recaptcha_load_callback = function() {
        window.recaptcha_is_loaded = true;
        };
    </script>
    
    <script
        src="https://www.recaptcha.net/recaptcha/enterprise.js?onload=on_recaptcha_load_callback&render=6LerBOgUAAAAAKPg6vsAFPTN66Woz-jBClxdQU-o"
        async defer>
    </script>
        <script type="text/javascript">
          
        </script>
    
        
    
        
      <style>
        
          background:url(https://cdn.robertsspaceindustries.com/static/images/noisebg.gif) repeat center top #000b11;
        
      </style>
    
        <link href="https://robertsspaceindustries.com/rsi/assets/fonts.css?family=Electrolize|Orbitron:400,500,700|Quantico|Share+Tech+Mono" rel="stylesheet" type="text/css">
    
        <link href="/cache/en/rsi-css.css?v=9.178.2" media="all" rel="stylesheet">
    
    
        <script 
        type="module" 
        data-cookieconsent="ignore" 
        src="https://robertsspaceindustries.com/plt-client/plt-client.es.js"
        data-platform-client-props="{&quot;lang&quot;:&quot;en&quot;,&quot;user&quot;:{&quot;isSignedIn&quot;:true,&quot;avatar&quot;:&quot;\/media\/0rixm629l5bwwr\/avatar\/A5ce2752-Ce33-446e-Ae18-2dab9f9ead8a.jpg&quot;,&quot;referral&quot;:{&quot;referralCode&quot;:&quot;STAR-73KP-54LB&quot;,&quot;referralUrl&quot;:&quot;https%3A%2F%2Frobertsspaceindustries.com%2Fenlist%3Freferral%3DSTAR-73KP-54LB&quot;,&quot;referralUrlCopy&quot;:&quot;https:\/\/robertsspaceindustries.com\/enlist?referral=STAR-73KP-54LB&quot;},&quot;useLegacyAccountPanel&quot;:false,&quot;isSubscriber&quot;:false,&quot;favorite&quot;:{&quot;img&quot;:&quot;https:\/\/media.robertsspaceindustries.com\/9qvh53v4nyx8d\/heap_note.png&quot;,&quot;name&quot;:&quot;Civilian&quot;},&quot;xsrfToken&quot;:{&quot;cookieName&quot;:&quot;Rsi-XSRF&quot;,&quot;token&quot;:&quot;edgQaA:fWuAImMepmSWIV6C9a4riA&quot;,&quot;ttlMargin&quot;:1800000,&quot;cookieValue&quot;:null}}}"
    ></script>
      </head>
    
        <body id="" class=""  lang=en localized=1>
        
              
    
        
                
    <div 
      data-rsi-component="PlatformBar.Data"
      data-rsi-component-props='{
        "root": "home",
        "active": "dyn_bd_first_level_IDS-Nanoart",
        "api": {
          "nav": {
            "url": "/nav/",
            "load": ["main","games","shop","explore","community","support","tools"]
          }
        },
        "nodes": {
                      "dyn_bd_first_level_IDS-Nanoart": {"slug":"dyn_bd_first_level_IDS-Nanoart","parent":"home","item":{"title":"IDS-Nanoart"}},
                      "home": {
            "toolbar": ["launcher-link"]
          },
                "buy-star-citizen": {
            "item": {
              "link": {
                "href": "\/download"
              }
            }
          },
          "subscribers": {"children":["subscription-become","subscribers-store"]},
          "subscribers-store": {"item":{"link":{"href":"\/store\/pledge\/browse\/extras\/subscribers-store"}}},
          "subscription": {"item":{"link":{"href":"\/pledge\/subscriptions"}}}
        },
        "layouts": {
          "store-all": null
        },
        "localeSelector": {
          "available": {
            "languages": ["en"]
          },
          "selected": {
            "language": "en"
          }
                ,"languages": {"en":{"code":"en","label":"English","codeLabel":"en","subLabel":null,"altCodes":null,"badges":[],"url":"\/en\/citizens\/IDS-Nanoart"}}
                      ,"currency": {"USD":{"iso":"USD","symbol":"$","label":"United States dollar"},"CAD":{"iso":"CAD","symbol":"$","label":"Canadian dollar"},"EUR":{"iso":"EUR","symbol":"\u20ac","label":"Euro"},"GBP":{"iso":"GBP","symbol":"\u00a3","label":"Pound sterling"}}
              },
            "tools": {
          "launcher-link": {
            "title": "Download",
            "href": "\/download"
          }
        },
        "translations": {
          "backToRSIMobile": "BACK TO RSI.com",
          "cancelButton": "Cancel",
          "confirmButton": "Confirm",
          "currencyTitle": "Currency",
          "languageTitle": "Language"
        }
      }'>
    </div>
    
    <div
        data-rsi-component="PlatformBar.Head"
        data-rsi-component-props='{
            "breadCrumbCurrentItem": null    }'
        data-orion-skin="default"
        data-orion-theme=""
    ></div>
    
      <div
        data-rsi-component="PlatformBar.Navigation"
        data-orion-skin="default"
        data-orion-theme=""
      ></div>
        
    
        <div id="bodyWrapper">
                <div id="platform-client-root"></div>
          
        
      <div class="page-wrapper">
        
        <div id="contentbody" class="public-profile public-profile-landing" style="">
          
      <div id="profile" class="wrapper">
        <h1 class="page-title ">
      <span class="top-line"></span>
      <span class="inner-line"></span>
      <span class="icon"></span>CITIZEN DOSSIER
      <span class="bottom-line"></span>
    </h1>    <div id="public-profile" class="account-profile">
              <div class="tabs tabs2">
            <div class="holder clearfix">
              <a href="/citizens/IDS-Nanoart" class="holotab active">
                <span class="text trans-02s">Overview</span>
                <span class="top trans-02s"></span>
                <span class="bottom trans-02s"></span>
              </a>
              <a href="/citizens/IDS-Nanoart/organizations" class="holotab right">
                <span class="text trans-02s">Organizations</span>
                <span class="top trans-02s"></span>
                <span class="bottom trans-02s"></span>
              </a>
            </div>
          </div>
          <div class="profile-content overview-content clearfix">
            <p class="entry citizen-record">
              <span class="label">UEE Citizen Record</span>
              <strong class="value">n/a</strong>
            </p>
            <div class="box-content profile-wrapper clearfix">
              <div class="inner-bg clearfix">
                <div class="profile left-col">
                  <span class="title">Profile </span>
                  <div class="inner clearfix">
                    <div class="thumb">
                      <img src="https://cdn.robertsspaceindustries.com/static/images/account/avatar_default_big.jpg" />
                      <span class="deco-corner top left"></span>
                      <span class="deco-corner top right"></span>
                      <span class="deco-corner bottom left"></span>
                      <span class="deco-corner bottom right"></span>
                    </div>
                    <div class="info">
                      <p class="entry">
                        <strong class="value">Nanoart</strong>
                      </p>
                      <p class="entry">
                        <span class="label">Handle name</span>
                        <strong class="value">IDS-Nanoart</strong>
                      </p>
                                          <p class="entry">
                                                  <span class="icon">
                              <img src="https://media.robertsspaceindustries.com/9qvh53v4nyx8d/heap_thumb.png"/>
                            </span>
                                                <span class="value">Civilian</span>
                        </p>
                                      </div>
                  </div>
                </div>
                <div class="main-org right-col visibility-V">
                  <span class="title">Main organization </span>
                  <div class="inner clearfix">
                                      <div class="thumb">
                                                                                      <a href="/orgs/IDSCORP"><img src="/media/9yuww3zgrjvw2r/heap_infobox/IDSCORP-Logo.png" /></a>
                                            <span class="deco-corner top left"></span>
                        <span class="deco-corner top right"></span>
                        <span class="deco-corner bottom left"></span>
                        <span class="deco-corner bottom right"></span>
                      </div>
                      <div class="info">
                        <p class="entry">
                                                <a href="/orgs/IDSCORP" class="value data14" style="background-position:-184px center">Invicta Corporation</a>
                        </p>
                        <p class="entry">
                                                <span class="label data10">Spectrum Identification (SID)</span>
                                                <strong class="value data10">IDSCORP</strong>
                        </p>
                        <p class="entry">
                                                <span class="label data3">Organization rank</span>
                                                <strong class="value data11">Expert</strong>
                        </p>
                        <div class="ranking data1">
                                                                            <span class="active"><span></span></span>
                                                      <span class="active"><span></span></span>
                                                      <span class="active"><span></span></span>
                                                      <span class="active"><span></span></span>
                                                      <span ><span></span></span>
                                                                      </div>
                      </div>
                                  </div>
                  <span class="deco-separator top"></span>
                  <span class="deco-separator bottom"></span>
                              </div>
              </div>
              <span class="deco-corner top left"></span>
              <span class="deco-corner top right"></span>
              <span class="deco-corner bottom left"></span>
              <span class="deco-corner bottom right"></span>
              <span class="deco-edge left"><span class="top"></span><span class="bottom"></span></span>
              <span class="deco-edge right"><span class="top"></span><span class="bottom"></span></span>
            </div>
            <div class="left-col">
              <div class="inner">
                <p class="entry">
                  <span class="label">Enlisted</span>
                  <strong class="value">Jan 21, 2022</strong>
                </p>
                              <p class="entry">
                    <span class="label">Location</span>
                    <strong class="value">
                      Thailand
                                          , Krung Thep Maha Nakhon [Bangkok]
                                      </strong>
                  </p>
                            <p class="entry">
                  <span class="label">Fluency</span>
                  <strong class="value">                                                  Thai                                </strong>
                </p>
              </div>
            </div>
            <div class="right-col">
              <div class="inner">
                                                                </div>
            </div>
                  </div>
        </div>
      </div>
    
        </div>
        
      </div>
    
      
    
    
    
                   <script id="tpl_number_counter_digits" type="text/x-jsmart-tmpl">{if !$seperator}{$seperator=','}{/if}
    {if !$first_max}{$first_max=9}{/if}
    {for $digit = 0 to $length-1}
      <div class="mask">
        <div class="carousel">
          {if $digit == 0}
            {$max = $first_max}
          {else}
            {$max = 9}
          {/if}
          {for $i=0 to $max}
            <div class="item {if $val_arr[$digit] == $i}on{/if}" rel="{$i}">{$i}</div>
          {/for}
        </div>
      </div>
      {if ($length - $digit) % 3 == 1 && $digit != $length-1}
      <div class="seperator">{$seperator}</div>
      {/if}
    {/for}</script>
    <script id="base_modal" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
      <div class="top-border">
        {block name="modal_lines"}
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        {/block}
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        {block name="modal_content"}{/block}
        {block name="modal_footer"}{/block}
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
        {block name="modal_lines"}
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        {/block}
      </div>
    </div></script>
    <script id="base_modal_flat" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
      
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        {block name="modal_content"}{/block}
        {block name="modal_footer"}{/block}
      </div>
      
    </div></script>
    <script id="tpl_modals_slideshow" type="text/x-jsmart-tmpl"><img class="top-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_top.png">
    <a href="" class="close js-close"></a>
    <div class="mask">
      <a class="js-prev prev control"></a>
      <a class="js-next next control"></a>
      <div class="slideshow-carousel carousel" rel="{$index}">
        {foreach from=$images item="image"}
          <div class="{if $index == $image@index}on{/if}">
          {if $image.is_video}
            <div class="video-holder">
              <div id="slideshow_video_{$image@index}" data-source="{$image->source_url}">
                <video width="100%" height="100%" preload="auto" {if $video}src="{$image->source_url}"{/if} controls></video>
              </div>
            </div>
          {else}
            <div class="media js-media-slideshow-{$image@iteration}">
            {if $image.low_res}
              <picture>
                <!--[if IE 9]><video style="display: none;"><![endif]-->
                <source data-srcset="{$image.full_res}" media="(min-width: 300px)" />
                <!--[if IE 9]></video><![endif]-->
                <img data-srcset="{$image.low_res}" alt="{$image.title}" />
              </picture>
            {else}
              <img data-src="{$image.source_url}" />
            {/if}
            </div>
          {/if}
            <div class="text">
              {if !$image.is_video}
              <a href="{$image.source_url}" class="download"></a>
              {/if}
              <div class="copyright">© 2012-{$year}<br />Cloud Imperium Games Corporation &<br />Roberts Space Industries Corp.</div>
              <div class="page-number">{$image@iteration} / {count($images)}</div>
              <div class="caption v-center">{if $image.title && $image.title != "undefined"}{$image.title}{/if}</div>
              <div class="cboth"></div>
            </div>
          </div>
        {/foreach}
      </div>
    </div>
    <img class="bottom-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_bottom.png"></script>
    <script id="tpl_contact_us" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
      <div class="top-border">
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        
    <div id="contact" class="inner-content on">
      <h2><span class="icon"></span>CONTACT</h2>
      <div class="padder">
        <div class="separator"></div>
        <form name="" action="" method="POST" class="legacy-form">
      <div class="error-message js-error-message"></div>
      <div class="success-message js-success-message"></div>
        <fieldset>
        <label for="contact_subject">Subject</label>
        <input type="text" name="subject" value="" class="trans-02s trans-color trans-box-shadow" id="contact_subject" />
        <label>Contacting us for:</label>
        <ul class="category-info">
                <li id="tech_support_info">Questions about download, installation, networking, or in-game client problems</li>
                <li id="subscription_info">Questions about monthly and yearly subscription plans</li>
                <li id="account_billing_info">Issues related to your account, such as incorrect information or ability to access account, or Billing with regards to payments and payment methods</li>
                <li id="melt_request_info">To reclaim a pledge over $1,000 for store credit (please note - this is a permanent action)</li>
                <li id="merchandise_info">Questions about physical and/or shipped merchandise</li>
                <li id="hacked_info">Issues related to compromised account or missing pledge.</li>
                <li id="account_recovery_info">For issues with account authentication, lost passwords and related queries</li>
                <li id="probation_info">Issues related to forums probation or ban</li>
                <li id="refund_request_info">Refund requests and related inquiries</li>
                <li id="customer_support_info">For general questions and queries regarding Star Citizen</li>
              </ul>
      </fieldset>
      <fieldset>
        <label for="contact_text">Description</label>
        <textarea name="text" class="trans-02s trans-color trans-box-shadow" id="contact_text"></textarea>
      </fieldset>
      <div class="contact-submit-wrapper">
        <div class="line"></div>
        <button class="submit js-submit"><strong>submit your message</strong></button>
      </div>
    </form>
        <div class="separator"></div>
      </div>
    </div>
    
        
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
      </div>
    </div></script>
    <script id="tpl_error" type="text/x-jsmart-tmpl"><div class="modal-error js-modal-error">
      <p class="modal-text js-modal-text"></p>
      <a class="close js-close trans-03s .trans-opacity" href=""></a>
    </div></script>
    <script id="tpl_success" type="text/x-jsmart-tmpl"><div class="modal-success js-modal-success">
      <p class="modal-text js-modal-text"></p>
      <a class="close js-close trans-03s .trans-opacity" href=""></a>
    </div></script>
    <script id="tpl_progress" type="text/x-jsmart-tmpl"><div class="modal-progress js-modal-progress">
      <div class="traj-loader">
        <div class="fast-blink"></div>
        <span class="modal-text js-modal-text"></span>
      </div>
    </div></script>
    <script id="tpl_outbound" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
      <div class="top-border">
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        
    <div id="outbound" class="inner-content on">
      <h2><span class="icon"></span>OUTBOUND LINK</h2>
      <div class="padder">
        <div class="separator"></div>
        <form name="" action="" method="POST" class="legacy-form">
          <div class="error-message js-error-message"> <span class=important>WARNING</span><br/><br/> This link will bring you outside of the RSI site and into the depths of the internet. Continue?<br/><br/><span class="url"></span> </div>
          <div class="success-message js-success-message"><span class=important>STAND BY</span><br/><br/> Initiating hyperlink.<br/><br/></div>
    
          <fieldset class="clearfix last">
            <span class="submit-wrapper">
              <span class="submit-hover trans-02s trans-opacity"></span>
              <input type="submit" value="WARP" class="trans-02s trans-color trans-background" />
            </span>
          </fieldset>
        </form>
        <div class="separator"></div>
      </div>
    </div>
    
        
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
      </div>
    </div></script>
    
    <script id="tpl_l-notification-bar" type="text/x-jsmart-tmpl"><div class="l-notification-bar js-notification-bar">
    
      <div class="l-notification-bar__watermark js-svg-inliner h-svg__logo-star-citizen"></div>
    
      <div class="l-notification-bar__boxes">
        {if !$viewedCookieNotif}
          <div class="l-notification-bar__box">
            {include file='tpl_c-notification'
              type='cookie'
              title='COOKIES:'
              message="Our website uses Google Analytics to analyze our traffic. <br/>To learn how you can control Google's use of your data and how you can opt out <a href='https://www.google.com/policies/privacy/partners/'>click here</a>."
              linkText='See Details'
              buttonText='Got it!'}
          </div>
        {/if}
    
        {if !$viewedPrivacyNotif}
          <div class="l-notification-bar__box">
            {include file='tpl_c-notification'
              type='privacy'
              title='PRIVACY POLICY:'
              message='We adjusted the PP to reflect the decision of the European Court of Justice regarding Safe Harbor, the fact that RSI has moved and added some services providers.'
              linkText='View Privacy Policy'
              buttonText='Got it!'}
          </div>
        {/if}
      </div>
    
    </div>
    </script>
    <script id="tpl_c-notification" type="text/x-jsmart-tmpl"><div class="c-notification js-bottom-notif-msg-{$type}">
        <div class="c-notification__title">{$title}</div>
        <div class="c-notification__message">
          {$message}
        </div>
    
        {if $linkText}
            <div class="c-notification__wrapper-link">
                <a class="c-notification__link js-bottom-notif-link-{$type}">
                {$linkText}
                </a>
            </div>
        {/if}
    
        <a class="c-notification__button js-bottom-notif-btn-{$type}">
    
          <span class="c-notification__button-text">
           {$buttonText}
          </span>
    
          {if $type neq 'announcement'}
            <div class="c-iconed__icon c-iconed__icon--checkmark"></div>
          {/if}
        </a>
    </div>
    </script>
    
    <script id="tpl_confirm" type="text/x-jsmart-tmpl"><div class="modal-confirm js-modal-confirm clearfix">
      <p class="modal-text js-modal-text"></p>
      <a class="bt-close js-close trans-03s trans-opacity" href=""></a>
      <a class="bt-confirm js-confirm trans-03s trans-opacity" href=""></a>
        <div class="buttons">
            <a class="shadow-button trans-02s trans-color js-close bt-close rm"     >
      <span class="label js-label trans-02s">Cancel</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
            <a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
      <span class="label js-label trans-02s">Confirm</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
        </div>
    </div>
    </script>
    <script id="tpl_alert" type="text/x-jsmart-tmpl"><div class="modal-alert js-modal-alert clearfix">
      <p class="modal-text js-modal-text"></p>
      <div class="buttons">
        <a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
      <span class="label js-label trans-02s">OK</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
      </div>
    </div></script>
    <script id="tpl_video" type="text/x-jsmart-tmpl">{extends file="base_modal"}
    {block name='modal_content'}
    <div id="ship-commercial" class="inner-content">
    
      <div class="hr"></div>
      <div class="content-block4">
    
        <div class="bottom"></div>
      </div>
      {if $distant_source=="vimeo"}
      <iframe id="commercial" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="//player.vimeo.com/video/{$video_id}?wmode=transparent" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>
      {else}
      <iframe id="commercial" frameborder="0" allowfullscreen="1" title="YouTube video player" width="100%" height="100%" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="https://www.youtube.com/embed/{$video_id}?autoplay=1"></iframe>
      {/if}
    </div>
    {/block}
    </script>
          
    
          
            
        
    
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KHNFZPT"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->
    
    
    <div data-rsi-component="PlatformFooter" data-rsi-component-props='{
      "currentSection": "rsi",
      "wscAbout": "/star-citizen",
      "wscPlay": "/playstarcitizen",
      "s42Game": "/squadron42",
      "s42Enlist": "/squadron42#enlist",
      "rsiCommlink": "/comm-link",
      "rsiCommunity": "/community-hub",
      "rsiRoadmap": "/roadmap",
      "showStoreMenu": "1",
      "isStoreMenuActive": "",
      "rsiStore": "/pledge",
      "rsiDownload": "/download",
      "isLauncherMenuActive": "",
      "rsiSpectrum": "/spectrum/community/SC",
      "showCitizenconMenu": "1",
      "rsiCitizencon": "/citizencon",
      "utilitiesHelp": "//support.robertsspaceindustries.com",
      "utilitiesPress": "/press",
      "utilitiesCareers": "https://cloudimperiumgames.com/join-us",
      "utilitiesAcknowledgement": "/acknowledgements",
      "utilitiesRedeemCode": "/pledge/redeem-code",
      "legalLegal": "/legal",
      "legalTos": "/tos",
      "legalPrivacy": "/privacy",
      "legalEula": "/eula",
      "legalDmca": "/dmca",
      "legalDisclosure": "/responsible-disclosure",
      "legalCaliforniaLegalNoticeAtCollection": "/privacy#california",
      "legalCaliforniaLegalPersonalInformation": "/cookies#preferences",
      "isConsentRequired": "",
      "clientRecordCountry": "GB",
      "cigLink": "https://cloudimperiumgames.com",
      "displayStarEngine": ""
    }'></div>
          
        </div>
      </body>
    </html>

    """

@pytest.fixture
def pilot_with_redacted_corp():
    return """ 
    <!DOCTYPE html>
        
    <html lang="en">
      <head>
            
        <script
        id="TagManager"
        data-cookieconsent="ignore"
        data-app-name="rsi-heap"
        data-app-version="9.181.0"
        data-category="account"
        data-sub-category="account-profile-public"
        src="/tag-manager/script.js"
        type="text/javascript"></script>
            <script
        type="text/javascript"
        id="Cookiebot"
        src="https://consent.cookiebot.com/uc.js"
        data-cbid="a687ee30-df65-45a0-9d22-90de6c1bb964"
        data-blockingmode="auto"
        data-georegions="{'region':'US-06,US-51,AT,BE,BG,HR,CY,CZ,DK,EE,FI,FR,DE,GR,HU,IE,IT,LV,LT,LU,MT,NL,PL,PT,RO,SK,SL,ES,SE','cbid':'a687ee30-df65-45a0-9d22-90de6c1bb964'}"></script>
        <script id="CookieConsent" src="/cookie-consent/script.js?async=false" type="text/javascript"></script>
      <link href="/rsi/static/css/cookiebot.css?v=9.181.0" rel="stylesheet" />
            <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    
        <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
        <meta name="description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans.">
    
        <meta name="csrf-token" content="9de548adfd3c7270d237683ea4ea2b174d51689a95e7352bb2325fd5bdabc7df" />
        <meta property="og:site_name" content="
    Black8y | Black8y - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
    " />
        <meta property="og:image" content="https://cdn.robertsspaceindustries.com/static/images/RSI-fb.jpg" />
        <meta property="og:description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans." />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://robertsspaceindustries.com/en/citizens/Black8y" />
        <meta property="og:locale" content="en" />
    
        <title>
    Black8y | Black8y - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
    </title>
    
        <link rel="canonical" href="https://robertsspaceindustries.com/en/citizens/Black8y">
    
        
                      <link rel="alternate" href="https://robertsspaceindustries.com/en/citizens/Black8y" hreflang="en">
                                
    
            <link rel=preconnect href="//sentry.turbulent.ca">
        <link rel=preconnect href="//gstatic.com">
        <link rel=preconnect href="//www.recaptcha.net">
        <link rel=preconnect href="//www.googletagmanager.com">
          
    
            <link href="/rsi/static/css/rsi-minimal.css?v=9.181.0" media="all" rel="stylesheet">
        
    <link href="/rsi/static/css/cross-brand-less.css?v=9.181.0" media="all" rel="stylesheet">
    
    
              
    <script type="text/javascript" src="/cache/en/rsi-external-js.js?v=9.181.0"></script>
    <script type="text/javascript" src="/cache/en/rsi-templates-js.js?v=9.181.0"></script>
    
            
              
    <link rel="stylesheet" href="https://use.typekit.net/dhw3beb.css">
    
    
    
              
    <script type="text/javascript" src='/rsi/static/packages/core/rsi.core.build.e8130.js'></script>
    <script type="text/javascript" src='/rsi/static/packages/account/rsi.account.build.74772.js'></script>
    <script type="text/javascript" src='/rsi/static/packages/store/rsi.store.build.0278b.js'></script>
    
    <script>
                    
        $(document).ready(function() {
        window.Common = new RSI.Common({});
        window.Main = new RSI.Main({
            'is_mobile': 0,
            'probation_cookie' : '',
            'require_captcha': 0
        });
        window.Mark = new Turbulent.Mark({ 'name' : 'Rsi-XSRF', 'token' : '+UcSaA:N6hNnq5TVN6I7EfQ+jDs9Q', 'ttl' : 1800 });
    
        window.WscOverlay = new RSI.WscOverlay({});
    
        var destinations = [];
    
    window.Main.destinations = destinations;    
        
        
        });
    
        $(window).load(function() {
        
        });
    </script>
    
    
        <script>
        window.recaptcha_is_loaded = false;
        window.on_recaptcha_load_callback = function() {
        window.recaptcha_is_loaded = true;
        };
    </script>
    
    <script
        src="https://www.recaptcha.net/recaptcha/enterprise.js?onload=on_recaptcha_load_callback&render=6LerBOgUAAAAAKPg6vsAFPTN66Woz-jBClxdQU-o"
        async defer>
    </script>
        <script type="text/javascript">
          
        </script>
    
        
    
        
      <style>
        
          background:url(https://cdn.robertsspaceindustries.com/static/images/noisebg.gif) repeat center top #000b11;
        
      </style>
    
        <link href="https://robertsspaceindustries.com/rsi/assets/fonts.css?family=Electrolize|Orbitron:400,500,700|Quantico|Share+Tech+Mono" rel="stylesheet" type="text/css">
    
        <link href="/cache/en/rsi-css.css?v=9.181.0" media="all" rel="stylesheet">
    
    
        <script 
        type="module" 
        data-cookieconsent="ignore" 
        src="https://robertsspaceindustries.com/plt-client/plt-client.es.js"
        data-platform-client-props="{&quot;lang&quot;:&quot;en&quot;,&quot;user&quot;:{&quot;isSignedIn&quot;:true,&quot;avatar&quot;:&quot;\/media\/0rixm629l5bwwr\/avatar\/A5ce2752-Ce33-446e-Ae18-2dab9f9ead8a.jpg&quot;,&quot;referral&quot;:{&quot;referralCode&quot;:&quot;STAR-73KP-54LB&quot;,&quot;referralUrl&quot;:&quot;https%3A%2F%2Frobertsspaceindustries.com%2Fenlist%3Freferral%3DSTAR-73KP-54LB&quot;,&quot;referralUrlCopy&quot;:&quot;https:\/\/robertsspaceindustries.com\/enlist?referral=STAR-73KP-54LB&quot;},&quot;useLegacyAccountPanel&quot;:false,&quot;isSubscriber&quot;:false,&quot;favorite&quot;:{&quot;img&quot;:&quot;https:\/\/media.robertsspaceindustries.com\/9qvh53v4nyx8d\/heap_thumb.png&quot;,&quot;name&quot;:&quot;Civilian&quot;},&quot;xsrfToken&quot;:{&quot;cookieName&quot;:&quot;Rsi-XSRF&quot;,&quot;token&quot;:&quot;+UcSaA:N6hNnq5TVN6I7EfQ+jDs9Q&quot;,&quot;ttlMargin&quot;:1800000,&quot;cookieValue&quot;:null}}}"
    ></script>
      </head>
    
        <body id="" class=""  lang=en localized=1>
        
              
    
        
                
    <div 
      data-rsi-component="PlatformBar.Data"
      data-rsi-component-props='{
        "root": "home",
        "active": "dyn_bd_first_level_Black8y",
        "api": {
          "nav": {
            "url": "/nav/",
            "load": ["main","games","shop","explore","community","support","tools"]
          }
        },
        "nodes": {
                      "dyn_bd_first_level_Black8y": {"slug":"dyn_bd_first_level_Black8y","parent":"home","item":{"title":"Black8y"}},
                      "home": {
            "toolbar": ["launcher-link"]
          },
                "buy-star-citizen": {
            "item": {
              "link": {
                "href": "\/download"
              }
            }
          },
          "subscribers": {"children":["subscription-become","subscribers-store"]},
          "subscribers-store": {"item":{"link":{"href":"\/store\/pledge\/browse\/extras\/subscribers-store"}}},
          "subscription": {"item":{"link":{"href":"\/pledge\/subscriptions"}}}
        },
        "layouts": {
          "store-all": null
        },
        "localeSelector": {
          "available": {
            "languages": ["en"]
          },
          "selected": {
            "language": "en"
          }
                ,"languages": {"en":{"code":"en","label":"English","codeLabel":"en","subLabel":null,"altCodes":null,"badges":[],"url":"\/en\/citizens\/Black8y"}}
                      ,"currency": {"USD":{"iso":"USD","symbol":"$","label":"United States dollar"},"CAD":{"iso":"CAD","symbol":"$","label":"Canadian dollar"},"EUR":{"iso":"EUR","symbol":"\u20ac","label":"Euro"},"GBP":{"iso":"GBP","symbol":"\u00a3","label":"Pound sterling"}}
              },
            "tools": {
          "launcher-link": {
            "title": "Download",
            "href": "\/download"
          }
        },
        "translations": {
          "backToRSIMobile": "BACK TO RSI.com",
          "cancelButton": "Cancel",
          "confirmButton": "Confirm",
          "currencyTitle": "Currency",
          "languageTitle": "Language"
        }
      }'>
    </div>
    
    <div
        data-rsi-component="PlatformBar.Head"
        data-rsi-component-props='{
            "breadCrumbCurrentItem": null    }'
        data-orion-skin="default"
        data-orion-theme=""
    ></div>
    
      <div
        data-rsi-component="PlatformBar.Navigation"
        data-orion-skin="default"
        data-orion-theme=""
      ></div>
        
    
        <div id="bodyWrapper">
                <div id="platform-client-root"></div>
          
        
      <div class="page-wrapper">
        
        <div id="contentbody" class="public-profile public-profile-landing" style="">
          
      <div id="profile" class="wrapper">
        <h1 class="page-title ">
      <span class="top-line"></span>
      <span class="inner-line"></span>
      <span class="icon"></span>CITIZEN DOSSIER
      <span class="bottom-line"></span>
    </h1>    <div id="public-profile" class="account-profile">
              <div class="tabs tabs2">
            <div class="holder clearfix">
              <a href="/citizens/Black8y" class="holotab active">
                <span class="text trans-02s">Overview</span>
                <span class="top trans-02s"></span>
                <span class="bottom trans-02s"></span>
              </a>
              <a href="/citizens/Black8y/organizations" class="holotab right">
                <span class="text trans-02s">Organizations</span>
                <span class="top trans-02s"></span>
                <span class="bottom trans-02s"></span>
              </a>
            </div>
          </div>
          <div class="profile-content overview-content clearfix">
            <p class="entry citizen-record">
              <span class="label">UEE Citizen Record</span>
              <strong class="value">#2369265</strong>
            </p>
            <div class="box-content profile-wrapper clearfix">
              <div class="inner-bg clearfix">
                <div class="profile left-col">
                  <span class="title">Profile </span>
                  <div class="inner clearfix">
                    <div class="thumb">
                      <img src="/media/n09milk6z9p8lr/heap_infobox/Gerardway_15624739_244180012683569_5910141282973384704_n.jpg" />
                      <span class="deco-corner top left"></span>
                      <span class="deco-corner top right"></span>
                      <span class="deco-corner bottom left"></span>
                      <span class="deco-corner bottom right"></span>
                    </div>
                    <div class="info">
                      <p class="entry">
                        <strong class="value">Black8y</strong>
                      </p>
                      <p class="entry">
                        <span class="label">Handle name</span>
                        <strong class="value">Black8y</strong>
                      </p>
                                          <p class="entry">
                                                  <span class="icon">
                              <img src="https://media.robertsspaceindustries.com/o43puk7vw95nn/heap_thumb.png"/>
                            </span>
                                                <span class="value">Swept Away</span>
                        </p>
                                      </div>
                  </div>
                </div>
                <div class="main-org right-col visibility-R">
                  <span class="title">Main organization </span>
                  <div class="inner clearfix">
                                      <div class="thumb">
                                                                                      <img src="https://cdn.robertsspaceindustries.com/static/images/organization/public-orgs-thumb-redacted-bg.png">
                                            <span class="deco-corner top left"></span>
                        <span class="deco-corner top right"></span>
                        <span class="deco-corner bottom left"></span>
                        <span class="deco-corner bottom right"></span>
                      </div>
                      <div class="info">
                        <p class="entry">
                                                <a href="" class="value data2" style="background-position:-208px center">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a>
                        </p>
                        <p class="entry">
                                                <span class="label data11">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
                                                <strong class="value data5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong>
                        </p>
                        <p class="entry">
                                                <span class="label data6">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
                                                <strong class="value data8">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong>
                        </p>
                        <div class="ranking data11">
                                              </div>
                      </div>
                                  </div>
                  <span class="deco-separator top"></span>
                  <span class="deco-separator bottom"></span>
                                  <div class="member-visibility-restriction member-visibility-r trans-03s">
                      <div class="restriction-r restriction"></div>
                    </div>
                              </div>
              </div>
              <span class="deco-corner top left"></span>
              <span class="deco-corner top right"></span>
              <span class="deco-corner bottom left"></span>
              <span class="deco-corner bottom right"></span>
              <span class="deco-edge left"><span class="top"></span><span class="bottom"></span></span>
              <span class="deco-edge right"><span class="top"></span><span class="bottom"></span></span>
            </div>
            <div class="left-col">
              <div class="inner">
                <p class="entry">
                  <span class="label">Enlisted</span>
                  <strong class="value">Sep 17, 2019</strong>
                </p>
                              <p class="entry">
                    <span class="label">Location</span>
                    <strong class="value">
                      China
                                          , Jiangsu
                                      </strong>
                  </p>
                            <p class="entry">
                  <span class="label">Fluency</span>
                  <strong class="value">                                                  English                                </strong>
                </p>
              </div>
            </div>
            <div class="right-col">
              <div class="inner">
                                                                </div>
            </div>
                  </div>
        </div>
      </div>
    
        </div>
        
      </div>
    
      
    
    
    
                   <script id="tpl_number_counter_digits" type="text/x-jsmart-tmpl">{if !$seperator}{$seperator=','}{/if}
    {if !$first_max}{$first_max=9}{/if}
    {for $digit = 0 to $length-1}
      <div class="mask">
        <div class="carousel">
          {if $digit == 0}
            {$max = $first_max}
          {else}
            {$max = 9}
          {/if}
          {for $i=0 to $max}
            <div class="item {if $val_arr[$digit] == $i}on{/if}" rel="{$i}">{$i}</div>
          {/for}
        </div>
      </div>
      {if ($length - $digit) % 3 == 1 && $digit != $length-1}
      <div class="seperator">{$seperator}</div>
      {/if}
    {/for}</script>
    <script id="base_modal" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
      <div class="top-border">
        {block name="modal_lines"}
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        {/block}
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        {block name="modal_content"}{/block}
        {block name="modal_footer"}{/block}
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
        {block name="modal_lines"}
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        {/block}
      </div>
    </div></script>
    <script id="base_modal_flat" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
      
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        {block name="modal_content"}{/block}
        {block name="modal_footer"}{/block}
      </div>
      
    </div></script>
    <script id="tpl_modals_slideshow" type="text/x-jsmart-tmpl"><img class="top-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_top.png">
    <a href="" class="close js-close"></a>
    <div class="mask">
      <a class="js-prev prev control"></a>
      <a class="js-next next control"></a>
      <div class="slideshow-carousel carousel" rel="{$index}">
        {foreach from=$images item="image"}
          <div class="{if $index == $image@index}on{/if}">
          {if $image.is_video}
            <div class="video-holder">
              <div id="slideshow_video_{$image@index}" data-source="{$image->source_url}">
                <video width="100%" height="100%" preload="auto" {if $video}src="{$image->source_url}"{/if} controls></video>
              </div>
            </div>
          {else}
            <div class="media js-media-slideshow-{$image@iteration}">
            {if $image.low_res}
              <picture>
                <!--[if IE 9]><video style="display: none;"><![endif]-->
                <source data-srcset="{$image.full_res}" media="(min-width: 300px)" />
                <!--[if IE 9]></video><![endif]-->
                <img data-srcset="{$image.low_res}" alt="{$image.title}" />
              </picture>
            {else}
              <img data-src="{$image.source_url}" />
            {/if}
            </div>
          {/if}
            <div class="text">
              {if !$image.is_video}
              <a href="{$image.source_url}" class="download"></a>
              {/if}
              <div class="copyright">© 2012-{$year}<br />Cloud Imperium Games Corporation &<br />Roberts Space Industries Corp.</div>
              <div class="page-number">{$image@iteration} / {count($images)}</div>
              <div class="caption v-center">{if $image.title && $image.title != "undefined"}{$image.title}{/if}</div>
              <div class="cboth"></div>
            </div>
          </div>
        {/foreach}
      </div>
    </div>
    <img class="bottom-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_bottom.png"></script>
    <script id="tpl_contact_us" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
      <div class="top-border">
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        
    <div id="contact" class="inner-content on">
      <h2><span class="icon"></span>CONTACT</h2>
      <div class="padder">
        <div class="separator"></div>
        <form name="" action="" method="POST" class="legacy-form">
      <div class="error-message js-error-message"></div>
      <div class="success-message js-success-message"></div>
        <fieldset>
        <label for="contact_subject">Subject</label>
        <input type="text" name="subject" value="" class="trans-02s trans-color trans-box-shadow" id="contact_subject" />
        <label>Contacting us for:</label>
        <ul class="category-info">
                <li id="tech_support_info">Questions about download, installation, networking, or in-game client problems</li>
                <li id="subscription_info">Questions about monthly and yearly subscription plans</li>
                <li id="account_billing_info">Issues related to your account, such as incorrect information or ability to access account, or Billing with regards to payments and payment methods</li>
                <li id="melt_request_info">To reclaim a pledge over $1,000 for store credit (please note - this is a permanent action)</li>
                <li id="merchandise_info">Questions about physical and/or shipped merchandise</li>
                <li id="hacked_info">Issues related to compromised account or missing pledge.</li>
                <li id="account_recovery_info">For issues with account authentication, lost passwords and related queries</li>
                <li id="probation_info">Issues related to forums probation or ban</li>
                <li id="refund_request_info">Refund requests and related inquiries</li>
                <li id="customer_support_info">For general questions and queries regarding Star Citizen</li>
              </ul>
      </fieldset>
      <fieldset>
        <label for="contact_text">Description</label>
        <textarea name="text" class="trans-02s trans-color trans-box-shadow" id="contact_text"></textarea>
      </fieldset>
      <div class="contact-submit-wrapper">
        <div class="line"></div>
        <button class="submit js-submit"><strong>submit your message</strong></button>
      </div>
    </form>
        <div class="separator"></div>
      </div>
    </div>
    
        
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
      </div>
    </div></script>
    <script id="tpl_error" type="text/x-jsmart-tmpl"><div class="modal-error js-modal-error">
      <p class="modal-text js-modal-text"></p>
      <a class="close js-close trans-03s .trans-opacity" href=""></a>
    </div></script>
    <script id="tpl_success" type="text/x-jsmart-tmpl"><div class="modal-success js-modal-success">
      <p class="modal-text js-modal-text"></p>
      <a class="close js-close trans-03s .trans-opacity" href=""></a>
    </div></script>
    <script id="tpl_progress" type="text/x-jsmart-tmpl"><div class="modal-progress js-modal-progress">
      <div class="traj-loader">
        <div class="fast-blink"></div>
        <span class="modal-text js-modal-text"></span>
      </div>
    </div></script>
    <script id="tpl_outbound" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
      <div class="top-border">
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
      </div>
      <div class="modal-inner">
        <a class="close js-close trans-03s .trans-opacity" href=""></a>
        
    <div id="outbound" class="inner-content on">
      <h2><span class="icon"></span>OUTBOUND LINK</h2>
      <div class="padder">
        <div class="separator"></div>
        <form name="" action="" method="POST" class="legacy-form">
          <div class="error-message js-error-message"> <span class=important>WARNING</span><br/><br/> This link will bring you outside of the RSI site and into the depths of the internet. Continue?<br/><br/><span class="url"></span> </div>
          <div class="success-message js-success-message"><span class=important>STAND BY</span><br/><br/> Initiating hyperlink.<br/><br/></div>
    
          <fieldset class="clearfix last">
            <span class="submit-wrapper">
              <span class="submit-hover trans-02s trans-opacity"></span>
              <input type="submit" value="WARP" class="trans-02s trans-color trans-background" />
            </span>
          </fieldset>
        </form>
        <div class="separator"></div>
      </div>
    </div>
    
        
      </div>
      <div class="bottom-border">
        <div class="h-border"></div>
        <div class="l-corner"></div>
        <div class="r-corner"></div>
        
        <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
        
      </div>
    </div></script>
    
    <script id="tpl_l-notification-bar" type="text/x-jsmart-tmpl"><div class="l-notification-bar js-notification-bar">
    
      <div class="l-notification-bar__watermark js-svg-inliner h-svg__logo-star-citizen"></div>
    
      <div class="l-notification-bar__boxes">
        {if !$viewedCookieNotif}
          <div class="l-notification-bar__box">
            {include file='tpl_c-notification'
              type='cookie'
              title='COOKIES:'
              message="Our website uses Google Analytics to analyze our traffic. <br/>To learn how you can control Google's use of your data and how you can opt out <a href='https://www.google.com/policies/privacy/partners/'>click here</a>."
              linkText='See Details'
              buttonText='Got it!'}
          </div>
        {/if}
    
        {if !$viewedPrivacyNotif}
          <div class="l-notification-bar__box">
            {include file='tpl_c-notification'
              type='privacy'
              title='PRIVACY POLICY:'
              message='We adjusted the PP to reflect the decision of the European Court of Justice regarding Safe Harbor, the fact that RSI has moved and added some services providers.'
              linkText='View Privacy Policy'
              buttonText='Got it!'}
          </div>
        {/if}
      </div>
    
    </div>
    </script>
    <script id="tpl_c-notification" type="text/x-jsmart-tmpl"><div class="c-notification js-bottom-notif-msg-{$type}">
        <div class="c-notification__title">{$title}</div>
        <div class="c-notification__message">
          {$message}
        </div>
    
        {if $linkText}
            <div class="c-notification__wrapper-link">
                <a class="c-notification__link js-bottom-notif-link-{$type}">
                {$linkText}
                </a>
            </div>
        {/if}
    
        <a class="c-notification__button js-bottom-notif-btn-{$type}">
    
          <span class="c-notification__button-text">
           {$buttonText}
          </span>
    
          {if $type neq 'announcement'}
            <div class="c-iconed__icon c-iconed__icon--checkmark"></div>
          {/if}
        </a>
    </div>
    </script>
    
    <script id="tpl_confirm" type="text/x-jsmart-tmpl"><div class="modal-confirm js-modal-confirm clearfix">
      <p class="modal-text js-modal-text"></p>
      <a class="bt-close js-close trans-03s trans-opacity" href=""></a>
      <a class="bt-confirm js-confirm trans-03s trans-opacity" href=""></a>
        <div class="buttons">
            <a class="shadow-button trans-02s trans-color js-close bt-close rm"     >
      <span class="label js-label trans-02s">Cancel</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
            <a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
      <span class="label js-label trans-02s">Confirm</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
        </div>
    </div>
    </script>
    <script id="tpl_alert" type="text/x-jsmart-tmpl"><div class="modal-alert js-modal-alert clearfix">
      <p class="modal-text js-modal-text"></p>
      <div class="buttons">
        <a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
      <span class="label js-label trans-02s">OK</span>
      <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
      <span class="left-section"></span>
      <span class="right-section"></span>
    </a>
      </div>
    </div></script>
    <script id="tpl_video" type="text/x-jsmart-tmpl">{extends file="base_modal"}
    {block name='modal_content'}
    <div id="ship-commercial" class="inner-content">
    
      <div class="hr"></div>
      <div class="content-block4">
    
        <div class="bottom"></div>
      </div>
      {if $distant_source=="vimeo"}
      <iframe id="commercial" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="//player.vimeo.com/video/{$video_id}?wmode=transparent" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>
      {else}
      <iframe id="commercial" frameborder="0" allowfullscreen="1" title="YouTube video player" width="100%" height="100%" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="https://www.youtube.com/embed/{$video_id}?autoplay=1"></iframe>
      {/if}
    </div>
    {/block}
    </script>
          
    
          
            
        
    
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KHNFZPT"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->
    
    
    <div data-rsi-component="PlatformFooter" data-rsi-component-props='{
      "currentSection": "rsi",
      "wscAbout": "/star-citizen",
      "wscPlay": "/playstarcitizen",
      "s42Game": "/squadron42",
      "s42Enlist": "/squadron42#enlist",
      "rsiCommlink": "/comm-link",
      "rsiCommunity": "/community-hub",
      "rsiRoadmap": "/roadmap",
      "showStoreMenu": "1",
      "isStoreMenuActive": "",
      "rsiStore": "/pledge",
      "rsiDownload": "/download",
      "isLauncherMenuActive": "",
      "rsiSpectrum": "/spectrum/community/SC",
      "showCitizenconMenu": "1",
      "rsiCitizencon": "/citizencon",
      "utilitiesHelp": "//support.robertsspaceindustries.com",
      "utilitiesPress": "/press",
      "utilitiesCareers": "https://cloudimperiumgames.com/join-us",
      "utilitiesAcknowledgement": "/acknowledgements",
      "utilitiesRedeemCode": "/pledge/redeem-code",
      "legalLegal": "/legal",
      "legalTos": "/tos",
      "legalPrivacy": "/privacy",
      "legalEula": "/eula",
      "legalDmca": "/dmca",
      "legalDisclosure": "/responsible-disclosure",
      "legalCaliforniaLegalNoticeAtCollection": "/privacy#california",
      "legalCaliforniaLegalPersonalInformation": "/cookies#preferences",
      "isConsentRequired": "",
      "clientRecordCountry": "GB",
      "cigLink": "https://cloudimperiumgames.com",
      "displayStarEngine": ""
    }'></div>
          
        </div>
      </body>
    </html>

    """

@pytest.fixture
def astrotemplar_player():
    return """
    
<!DOCTYPE html>
    
<html lang="en">
  <head>
        
    <script
    id="TagManager"
    data-cookieconsent="ignore"
    data-app-name="rsi-heap"
    data-app-version="9.184.0"
    data-category="account"
    data-sub-category="account-profile-public"
    src="/tag-manager/script.js"
    type="text/javascript"></script>
        <script
    type="text/javascript"
    id="Cookiebot"
    src="https://consent.cookiebot.com/uc.js"
    data-cbid="a687ee30-df65-45a0-9d22-90de6c1bb964"
    data-blockingmode="auto"
    data-georegions="{'region':'US-06,US-51,AT,BE,BG,HR,CY,CZ,DK,EE,FI,FR,DE,GR,HU,IE,IT,LV,LT,LU,MT,NL,PL,PT,RO,SK,SL,ES,SE','cbid':'a687ee30-df65-45a0-9d22-90de6c1bb964'}"></script>
    <script id="CookieConsent" src="/cookie-consent/script.js?async=false" type="text/javascript"></script>
  <link href="/rsi/static/css/cookiebot.css?v=9.184.0" rel="stylesheet" />
        <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
    <meta name="description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans.">

    <meta name="csrf-token" content="9de548adfd3c7270d237683ea4ea2b174d51689a95e7352bb2325fd5bdabc7df" />
    <meta property="og:site_name" content="
AstroTemplar | AstroTemplar - psi templars | PSITEMPLAR (Chamberlain) - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
" />
    <meta property="og:image" content="https://cdn.robertsspaceindustries.com/static/images/RSI-fb.jpg" />
    <meta property="og:description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans." />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://robertsspaceindustries.com/en/citizens/AstroTemplar" />
    <meta property="og:locale" content="en" />

    <title>
AstroTemplar | AstroTemplar - psi templars | PSITEMPLAR (Chamberlain) - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
</title>

    <link rel="canonical" href="https://robertsspaceindustries.com/en/citizens/AstroTemplar">

    
                  <link rel="alternate" href="https://robertsspaceindustries.com/en/citizens/AstroTemplar" hreflang="en">
                            

        <link rel=preconnect href="//sentry.turbulent.ca">
    <link rel=preconnect href="//gstatic.com">
    <link rel=preconnect href="//www.recaptcha.net">
    <link rel=preconnect href="//www.googletagmanager.com">
      

        <link href="/rsi/static/css/rsi-minimal.css?v=9.184.0" media="all" rel="stylesheet">
    
<link href="/rsi/static/css/cross-brand-less.css?v=9.184.0" media="all" rel="stylesheet">


          
<script type="text/javascript" src="/cache/en/rsi-external-js.js?v=9.184.0"></script>
<script type="text/javascript" src="/cache/en/rsi-templates-js.js?v=9.184.0"></script>

        
          
<link rel="stylesheet" href="https://use.typekit.net/dhw3beb.css">



          
<script type="text/javascript" src='/rsi/static/packages/core/rsi.core.build.e8130.js'></script>
<script type="text/javascript" src='/rsi/static/packages/account/rsi.account.build.74772.js'></script>
<script type="text/javascript" src='/rsi/static/packages/store/rsi.store.build.0278b.js'></script>

<script>
                
    $(document).ready(function() {
    window.Common = new RSI.Common({});
    window.Main = new RSI.Main({
        'is_mobile': 0,
        'probation_cookie' : '',
        'require_captcha': 0
    });
    window.Mark = new Turbulent.Mark({ 'name' : 'Rsi-XSRF', 'token' : 's4gTaA:z8g7J+fxKGMgPEp2INn7fA', 'ttl' : 1800 });

    window.WscOverlay = new RSI.WscOverlay({});

    var destinations = [];

window.Main.destinations = destinations;    
    
    
    });

    $(window).load(function() {
    
    });
</script>


    <script>
    window.recaptcha_is_loaded = false;
    window.on_recaptcha_load_callback = function() {
    window.recaptcha_is_loaded = true;
    };
</script>

<script
    src="https://www.recaptcha.net/recaptcha/enterprise.js?onload=on_recaptcha_load_callback&render=6LerBOgUAAAAAKPg6vsAFPTN66Woz-jBClxdQU-o"
    async defer>
</script>
    <script type="text/javascript">
      
    </script>

    

    
  <style>
    
      background:url(https://cdn.robertsspaceindustries.com/static/images/noisebg.gif) repeat center top #000b11;
    
  </style>

    <link href="https://robertsspaceindustries.com/rsi/assets/fonts.css?family=Electrolize|Orbitron:400,500,700|Quantico|Share+Tech+Mono" rel="stylesheet" type="text/css">

    <link href="/cache/en/rsi-css.css?v=9.184.0" media="all" rel="stylesheet">


    <script 
    type="module" 
    data-cookieconsent="ignore" 
    src="https://robertsspaceindustries.com/plt-client/plt-client.es.js"
    data-platform-client-props="{&quot;lang&quot;:&quot;en&quot;,&quot;user&quot;:{&quot;isSignedIn&quot;:true,&quot;avatar&quot;:&quot;\/media\/0rixm629l5bwwr\/avatar\/A5ce2752-Ce33-446e-Ae18-2dab9f9ead8a.jpg&quot;,&quot;referral&quot;:{&quot;referralCode&quot;:&quot;STAR-73KP-54LB&quot;,&quot;referralUrl&quot;:&quot;https%3A%2F%2Frobertsspaceindustries.com%2Fenlist%3Freferral%3DSTAR-73KP-54LB&quot;,&quot;referralUrlCopy&quot;:&quot;https:\/\/robertsspaceindustries.com\/enlist?referral=STAR-73KP-54LB&quot;},&quot;useLegacyAccountPanel&quot;:false,&quot;isSubscriber&quot;:false,&quot;favorite&quot;:{&quot;img&quot;:&quot;https:\/\/media.robertsspaceindustries.com\/9qvh53v4nyx8d\/heap_thumb.png&quot;,&quot;name&quot;:&quot;Civilian&quot;},&quot;xsrfToken&quot;:{&quot;cookieName&quot;:&quot;Rsi-XSRF&quot;,&quot;token&quot;:&quot;s4gTaA:z8g7J+fxKGMgPEp2INn7fA&quot;,&quot;ttlMargin&quot;:1800000,&quot;cookieValue&quot;:null}}}"
></script>
  </head>

    <body id="" class=""  lang=en localized=1>
    
          

    
            
<div 
  data-rsi-component="PlatformBar.Data"
  data-rsi-component-props='{
    "root": "home",
    "active": "dyn_bd_first_level_AstroTemplar",
    "api": {
      "nav": {
        "url": "/nav/",
        "load": ["main","games","shop","explore","community","support","tools"]
      }
    },
    "nodes": {
                  "dyn_bd_first_level_AstroTemplar": {"slug":"dyn_bd_first_level_AstroTemplar","parent":"home","item":{"title":"AstroTemplar"}},
                  "home": {
        "toolbar": ["launcher-link"]
      },
            "buy-star-citizen": {
        "item": {
          "link": {
            "href": "\/download"
          }
        }
      },
      "subscribers": {"children":["subscription-become","subscribers-store"]},
      "subscribers-store": {"item":{"link":{"href":"\/store\/pledge\/browse\/extras\/subscribers-store"}}},
      "subscription": {"item":{"link":{"href":"\/pledge\/subscriptions"}}}
    },
    "layouts": {
      "store-all": null
    },
    "localeSelector": {
      "available": {
        "languages": ["en"]
      },
      "selected": {
        "language": "en"
      }
            ,"languages": {"en":{"code":"en","label":"English","codeLabel":"en","subLabel":null,"altCodes":null,"badges":[],"url":"\/en\/citizens\/AstroTemplar"}}
                  ,"currency": {"USD":{"iso":"USD","symbol":"$","label":"United States dollar"},"CAD":{"iso":"CAD","symbol":"$","label":"Canadian dollar"},"EUR":{"iso":"EUR","symbol":"\u20ac","label":"Euro"},"GBP":{"iso":"GBP","symbol":"\u00a3","label":"Pound sterling"}}
          },
        "tools": {
      "launcher-link": {
        "title": "Download",
        "href": "\/download"
      }
    },
    "translations": {
      "backToRSIMobile": "BACK TO RSI.com",
      "cancelButton": "Cancel",
      "confirmButton": "Confirm",
      "currencyTitle": "Currency",
      "languageTitle": "Language"
    }
  }'>
</div>

<div
    data-rsi-component="PlatformBar.Head"
    data-rsi-component-props='{
        "breadCrumbCurrentItem": null    }'
    data-orion-skin="default"
    data-orion-theme=""
></div>

  <div
    data-rsi-component="PlatformBar.Navigation"
    data-orion-skin="default"
    data-orion-theme=""
  ></div>
    

    <div id="bodyWrapper">
            <div id="platform-client-root"></div>
      
    
  <div class="page-wrapper">
    
    <div id="contentbody" class="public-profile public-profile-landing" style="">
      
  <div id="profile" class="wrapper">
    <h1 class="page-title ">
  <span class="top-line"></span>
  <span class="inner-line"></span>
  <span class="icon"></span>CITIZEN DOSSIER
  <span class="bottom-line"></span>
</h1>    <div id="public-profile" class="account-profile">
          <div class="tabs tabs2">
        <div class="holder clearfix">
          <a href="/citizens/AstroTemplar" class="holotab active">
            <span class="text trans-02s">Overview</span>
            <span class="top trans-02s"></span>
            <span class="bottom trans-02s"></span>
          </a>
          <a href="/citizens/AstroTemplar/organizations" class="holotab right">
            <span class="text trans-02s">Organizations</span>
            <span class="top trans-02s"></span>
            <span class="bottom trans-02s"></span>
          </a>
        </div>
      </div>
      <div class="profile-content overview-content clearfix">
        <p class="entry citizen-record">
          <span class="label">UEE Citizen Record</span>
          <strong class="value">#622244</strong>
        </p>
        <div class="box-content profile-wrapper clearfix">
          <div class="inner-bg clearfix">
            <div class="profile left-col">
              <span class="title">Profile </span>
              <div class="inner clearfix">
                <div class="thumb">
                  <img src="/media/eed9f573atppnr/heap_infobox/13892446214927.jpg" />
                  <span class="deco-corner top left"></span>
                  <span class="deco-corner top right"></span>
                  <span class="deco-corner bottom left"></span>
                  <span class="deco-corner bottom right"></span>
                </div>
                <div class="info">
                  <p class="entry">
                    <strong class="value">AstroTemplar</strong>
                  </p>
                  <p class="entry">
                    <span class="label">Handle name</span>
                    <strong class="value">AstroTemplar</strong>
                  </p>
                                      <p class="entry">
                                              <span class="icon">
                          <img src="https://media.robertsspaceindustries.com/h7e4c5zryjjf2/heap_thumb.png"/>
                        </span>
                                            <span class="value">Wing Commander</span>
                    </p>
                                  </div>
              </div>
            </div>
            <div class="main-org right-col visibility-V">
              <span class="title">Main organization </span>
              <div class="inner clearfix">
                                  <div class="thumb">
                                                                                  <a href="/orgs/PSITEMPLAR"><img src="https://cdn.robertsspaceindustries.com/static/images/organization/defaults/logo/faith.jpg" /></a>
                                        <span class="deco-corner top left"></span>
                    <span class="deco-corner top right"></span>
                    <span class="deco-corner bottom left"></span>
                    <span class="deco-corner bottom right"></span>
                  </div>
                  <div class="info">
                    <p class="entry">
                                            <a href="/orgs/PSITEMPLAR" class="value data10" style="background-position:-297px center">psi templars</a>
                    </p>
                    <p class="entry">
                                            <span class="label data2">Spectrum Identification (SID)</span>
                                            <strong class="value data5">PSITEMPLAR</strong>
                    </p>
                    <p class="entry">
                                            <span class="label data14">Organization rank</span>
                                            <strong class="value data8">Chamberlain</strong>
                    </p>
                    <div class="ranking data11">
                                                                        <span class="active"><span></span></span>
                                                  <span class="active"><span></span></span>
                                                  <span class="active"><span></span></span>
                                                  <span class="active"><span></span></span>
                                                  <span class="active"><span></span></span>
                                                                  </div>
                  </div>
                              </div>
              <span class="deco-separator top"></span>
              <span class="deco-separator bottom"></span>
                          </div>
          </div>
          <span class="deco-corner top left"></span>
          <span class="deco-corner top right"></span>
          <span class="deco-corner bottom left"></span>
          <span class="deco-corner bottom right"></span>
          <span class="deco-edge left"><span class="top"></span><span class="bottom"></span></span>
          <span class="deco-edge right"><span class="top"></span><span class="bottom"></span></span>
        </div>
        <div class="left-col">
          <div class="inner">
            <p class="entry">
              <span class="label">Enlisted</span>
              <strong class="value">Oct 15, 2014</strong>
            </p>
                        <p class="entry">
              <span class="label">Fluency</span>
              <strong class="value">                                                  English                                </strong>
            </p>
          </div>
        </div>
        <div class="right-col">
          <div class="inner">
                                                    <div class="entry bio">
                <span class="label">Bio</span>
                <div class="value">
                  <br />
\m/ @(*_*)@ \m/
                </div>
              </div>
                                    </div>
        </div>
              </div>
    </div>
  </div>

    </div>
    
  </div>

  



               <script id="tpl_number_counter_digits" type="text/x-jsmart-tmpl">{if !$seperator}{$seperator=','}{/if}
{if !$first_max}{$first_max=9}{/if}
{for $digit = 0 to $length-1}
  <div class="mask">
    <div class="carousel">
      {if $digit == 0}
        {$max = $first_max}
      {else}
        {$max = 9}
      {/if}
      {for $i=0 to $max}
        <div class="item {if $val_arr[$digit] == $i}on{/if}" rel="{$i}">{$i}</div>
      {/for}
    </div>
  </div>
  {if ($length - $digit) % 3 == 1 && $digit != $length-1}
  <div class="seperator">{$seperator}</div>
  {/if}
{/for}</script>
<script id="base_modal" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
  <div class="top-border">
    {block name="modal_lines"}
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    {/block}
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
  </div>
  <div class="modal-inner">
    <a class="close js-close trans-03s .trans-opacity" href=""></a>
    {block name="modal_content"}{/block}
    {block name="modal_footer"}{/block}
  </div>
  <div class="bottom-border">
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
    {block name="modal_lines"}
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    {/block}
  </div>
</div></script>
<script id="base_modal_flat" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
  
  <div class="modal-inner">
    <a class="close js-close trans-03s .trans-opacity" href=""></a>
    {block name="modal_content"}{/block}
    {block name="modal_footer"}{/block}
  </div>
  
</div></script>
<script id="tpl_modals_slideshow" type="text/x-jsmart-tmpl"><img class="top-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_top.png">
<a href="" class="close js-close"></a>
<div class="mask">
  <a class="js-prev prev control"></a>
  <a class="js-next next control"></a>
  <div class="slideshow-carousel carousel" rel="{$index}">
    {foreach from=$images item="image"}
      <div class="{if $index == $image@index}on{/if}">
      {if $image.is_video}
        <div class="video-holder">
          <div id="slideshow_video_{$image@index}" data-source="{$image->source_url}">
            <video width="100%" height="100%" preload="auto" {if $video}src="{$image->source_url}"{/if} controls></video>
          </div>
        </div>
      {else}
        <div class="media js-media-slideshow-{$image@iteration}">
        {if $image.low_res}
          <picture>
            <!--[if IE 9]><video style="display: none;"><![endif]-->
            <source data-srcset="{$image.full_res}" media="(min-width: 300px)" />
            <!--[if IE 9]></video><![endif]-->
            <img data-srcset="{$image.low_res}" alt="{$image.title}" />
          </picture>
        {else}
          <img data-src="{$image.source_url}" />
        {/if}
        </div>
      {/if}
        <div class="text">
          {if !$image.is_video}
          <a href="{$image.source_url}" class="download"></a>
          {/if}
          <div class="copyright">© 2012-{$year}<br />Cloud Imperium Games Corporation &<br />Roberts Space Industries Corp.</div>
          <div class="page-number">{$image@iteration} / {count($images)}</div>
          <div class="caption v-center">{if $image.title && $image.title != "undefined"}{$image.title}{/if}</div>
          <div class="cboth"></div>
        </div>
      </div>
    {/foreach}
  </div>
</div>
<img class="bottom-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_bottom.png"></script>
<script id="tpl_contact_us" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
  <div class="top-border">
    
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
  </div>
  <div class="modal-inner">
    <a class="close js-close trans-03s .trans-opacity" href=""></a>
    
<div id="contact" class="inner-content on">
  <h2><span class="icon"></span>CONTACT</h2>
  <div class="padder">
    <div class="separator"></div>
    <form name="" action="" method="POST" class="legacy-form">
  <div class="error-message js-error-message"></div>
  <div class="success-message js-success-message"></div>
    <fieldset>
    <label for="contact_subject">Subject</label>
    <input type="text" name="subject" value="" class="trans-02s trans-color trans-box-shadow" id="contact_subject" />
    <label>Contacting us for:</label>
    <ul class="category-info">
            <li id="tech_support_info">Questions about download, installation, networking, or in-game client problems</li>
            <li id="subscription_info">Questions about monthly and yearly subscription plans</li>
            <li id="account_billing_info">Issues related to your account, such as incorrect information or ability to access account, or Billing with regards to payments and payment methods</li>
            <li id="melt_request_info">To reclaim a pledge over $1,000 for store credit (please note - this is a permanent action)</li>
            <li id="merchandise_info">Questions about physical and/or shipped merchandise</li>
            <li id="hacked_info">Issues related to compromised account or missing pledge.</li>
            <li id="account_recovery_info">For issues with account authentication, lost passwords and related queries</li>
            <li id="probation_info">Issues related to forums probation or ban</li>
            <li id="refund_request_info">Refund requests and related inquiries</li>
            <li id="customer_support_info">For general questions and queries regarding Star Citizen</li>
          </ul>
  </fieldset>
  <fieldset>
    <label for="contact_text">Description</label>
    <textarea name="text" class="trans-02s trans-color trans-box-shadow" id="contact_text"></textarea>
  </fieldset>
  <div class="contact-submit-wrapper">
    <div class="line"></div>
    <button class="submit js-submit"><strong>submit your message</strong></button>
  </div>
</form>
    <div class="separator"></div>
  </div>
</div>

    
  </div>
  <div class="bottom-border">
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
    
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    
  </div>
</div></script>
<script id="tpl_error" type="text/x-jsmart-tmpl"><div class="modal-error js-modal-error">
  <p class="modal-text js-modal-text"></p>
  <a class="close js-close trans-03s .trans-opacity" href=""></a>
</div></script>
<script id="tpl_success" type="text/x-jsmart-tmpl"><div class="modal-success js-modal-success">
  <p class="modal-text js-modal-text"></p>
  <a class="close js-close trans-03s .trans-opacity" href=""></a>
</div></script>
<script id="tpl_progress" type="text/x-jsmart-tmpl"><div class="modal-progress js-modal-progress">
  <div class="traj-loader">
    <div class="fast-blink"></div>
    <span class="modal-text js-modal-text"></span>
  </div>
</div></script>
<script id="tpl_outbound" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
  <div class="top-border">
    
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
  </div>
  <div class="modal-inner">
    <a class="close js-close trans-03s .trans-opacity" href=""></a>
    
<div id="outbound" class="inner-content on">
  <h2><span class="icon"></span>OUTBOUND LINK</h2>
  <div class="padder">
    <div class="separator"></div>
    <form name="" action="" method="POST" class="legacy-form">
      <div class="error-message js-error-message"> <span class=important>WARNING</span><br/><br/> This link will bring you outside of the RSI site and into the depths of the internet. Continue?<br/><br/><span class="url"></span> </div>
      <div class="success-message js-success-message"><span class=important>STAND BY</span><br/><br/> Initiating hyperlink.<br/><br/></div>

      <fieldset class="clearfix last">
        <span class="submit-wrapper">
          <span class="submit-hover trans-02s trans-opacity"></span>
          <input type="submit" value="WARP" class="trans-02s trans-color trans-background" />
        </span>
      </fieldset>
    </form>
    <div class="separator"></div>
  </div>
</div>

    
  </div>
  <div class="bottom-border">
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
    
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    
  </div>
</div></script>

<script id="tpl_l-notification-bar" type="text/x-jsmart-tmpl"><div class="l-notification-bar js-notification-bar">

  <div class="l-notification-bar__watermark js-svg-inliner h-svg__logo-star-citizen"></div>

  <div class="l-notification-bar__boxes">
    {if !$viewedCookieNotif}
      <div class="l-notification-bar__box">
        {include file='tpl_c-notification'
          type='cookie'
          title='COOKIES:'
          message="Our website uses Google Analytics to analyze our traffic. <br/>To learn how you can control Google's use of your data and how you can opt out <a href='https://www.google.com/policies/privacy/partners/'>click here</a>."
          linkText='See Details'
          buttonText='Got it!'}
      </div>
    {/if}

    {if !$viewedPrivacyNotif}
      <div class="l-notification-bar__box">
        {include file='tpl_c-notification'
          type='privacy'
          title='PRIVACY POLICY:'
          message='We adjusted the PP to reflect the decision of the European Court of Justice regarding Safe Harbor, the fact that RSI has moved and added some services providers.'
          linkText='View Privacy Policy'
          buttonText='Got it!'}
      </div>
    {/if}
  </div>

</div>
</script>
<script id="tpl_c-notification" type="text/x-jsmart-tmpl"><div class="c-notification js-bottom-notif-msg-{$type}">
    <div class="c-notification__title">{$title}</div>
    <div class="c-notification__message">
      {$message}
    </div>

    {if $linkText}
        <div class="c-notification__wrapper-link">
            <a class="c-notification__link js-bottom-notif-link-{$type}">
            {$linkText}
            </a>
        </div>
    {/if}

    <a class="c-notification__button js-bottom-notif-btn-{$type}">

      <span class="c-notification__button-text">
       {$buttonText}
      </span>

      {if $type neq 'announcement'}
        <div class="c-iconed__icon c-iconed__icon--checkmark"></div>
      {/if}
    </a>
</div>
</script>

<script id="tpl_confirm" type="text/x-jsmart-tmpl"><div class="modal-confirm js-modal-confirm clearfix">
  <p class="modal-text js-modal-text"></p>
  <a class="bt-close js-close trans-03s trans-opacity" href=""></a>
  <a class="bt-confirm js-confirm trans-03s trans-opacity" href=""></a>
	<div class="buttons">
		<a class="shadow-button trans-02s trans-color js-close bt-close rm"     >
  <span class="label js-label trans-02s">Cancel</span>
  <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
  <span class="left-section"></span>
  <span class="right-section"></span>
</a>
		<a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
  <span class="label js-label trans-02s">Confirm</span>
  <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
  <span class="left-section"></span>
  <span class="right-section"></span>
</a>
	</div>
</div>
</script>
<script id="tpl_alert" type="text/x-jsmart-tmpl"><div class="modal-alert js-modal-alert clearfix">
  <p class="modal-text js-modal-text"></p>
  <div class="buttons">
    <a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
  <span class="label js-label trans-02s">OK</span>
  <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
  <span class="left-section"></span>
  <span class="right-section"></span>
</a>
  </div>
</div></script>
<script id="tpl_video" type="text/x-jsmart-tmpl">{extends file="base_modal"}
{block name='modal_content'}
<div id="ship-commercial" class="inner-content">

  <div class="hr"></div>
  <div class="content-block4">

    <div class="bottom"></div>
  </div>
  {if $distant_source=="vimeo"}
  <iframe id="commercial" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="//player.vimeo.com/video/{$video_id}?wmode=transparent" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>
  {else}
  <iframe id="commercial" frameborder="0" allowfullscreen="1" title="YouTube video player" width="100%" height="100%" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="https://www.youtube.com/embed/{$video_id}?autoplay=1"></iframe>
  {/if}
</div>
{/block}
</script>
      

      
        
    

<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KHNFZPT"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->


<div data-rsi-component="PlatformFooter" data-rsi-component-props='{
  "currentSection": "rsi",
  "wscAbout": "/star-citizen",
  "wscPlay": "/playstarcitizen",
  "s42Game": "/squadron42",
  "s42Enlist": "/squadron42#enlist",
  "rsiCommlink": "/comm-link",
  "rsiCommunity": "/community-hub",
  "rsiRoadmap": "/roadmap",
  "showStoreMenu": "1",
  "isStoreMenuActive": "",
  "rsiStore": "/pledge",
  "rsiDownload": "/download",
  "isLauncherMenuActive": "",
  "rsiSpectrum": "/spectrum/community/SC",
  "showCitizenconMenu": "1",
  "rsiCitizencon": "/citizencon",
  "utilitiesHelp": "//support.robertsspaceindustries.com",
  "utilitiesPress": "/press",
  "utilitiesCareers": "https://cloudimperiumgames.com/join-us",
  "utilitiesAcknowledgement": "/acknowledgements",
  "utilitiesRedeemCode": "/pledge/redeem-code",
  "legalLegal": "/legal",
  "legalTos": "/tos",
  "legalPrivacy": "/privacy",
  "legalEula": "/eula",
  "legalDmca": "/dmca",
  "legalDisclosure": "/responsible-disclosure",
  "legalCaliforniaLegalNoticeAtCollection": "/privacy#california",
  "legalCaliforniaLegalPersonalInformation": "/cookies#preferences",
  "isConsentRequired": "",
  "clientRecordCountry": "GB",
  "cigLink": "https://cloudimperiumgames.com",
  "displayStarEngine": ""
}'></div>
      
    </div>
  </body>
</html>
"""

@pytest.fixture
def pilot_with_more_than_one_fluency():
    return """
    
<!DOCTYPE html>
    
<html lang="en">
  <head>
        
    <script
    id="TagManager"
    data-cookieconsent="ignore"
    data-app-name="rsi-heap"
    data-app-version="9.185.0"
    data-category="account"
    data-sub-category="account-profile-public"
    src="/tag-manager/script.js"
    type="text/javascript"></script>
        <script
    type="text/javascript"
    id="Cookiebot"
    src="https://consent.cookiebot.com/uc.js"
    data-cbid="a687ee30-df65-45a0-9d22-90de6c1bb964"
    data-blockingmode="auto"
    data-georegions="{'region':'US-06,US-51,AT,BE,BG,HR,CY,CZ,DK,EE,FI,FR,DE,GR,HU,IE,IT,LV,LT,LU,MT,NL,PL,PT,RO,SK,SL,ES,SE','cbid':'a687ee30-df65-45a0-9d22-90de6c1bb964'}"></script>
    <script id="CookieConsent" src="/cookie-consent/script.js?async=false" type="text/javascript"></script>
  <link href="/rsi/static/css/cookiebot.css?v=9.185.0" rel="stylesheet" />
        <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
    <meta name="description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans.">

    <meta name="csrf-token" content="9de548adfd3c7270d237683ea4ea2b174d51689a95e7352bb2325fd5bdabc7df" />
    <meta property="og:site_name" content="
Arrisan Amoria | Arrisan_Amoria - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
" />
    <meta property="og:image" content="https://cdn.robertsspaceindustries.com/static/images/RSI-fb.jpg" />
    <meta property="og:description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans." />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://robertsspaceindustries.com/en/citizens/Arrisan_Amoria" />
    <meta property="og:locale" content="en" />

    <title>
Arrisan Amoria | Arrisan_Amoria - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
</title>

    <link rel="canonical" href="https://robertsspaceindustries.com/en/citizens/Arrisan_Amoria">

    
                  <link rel="alternate" href="https://robertsspaceindustries.com/en/citizens/Arrisan_Amoria" hreflang="en">
                            

        <link rel=preconnect href="//sentry.turbulent.ca">
    <link rel=preconnect href="//gstatic.com">
    <link rel=preconnect href="//www.recaptcha.net">
    <link rel=preconnect href="//www.googletagmanager.com">
      

        <link href="/rsi/static/css/rsi-minimal.css?v=9.185.0" media="all" rel="stylesheet">
    
<link href="/rsi/static/css/cross-brand-less.css?v=9.185.0" media="all" rel="stylesheet">


          
<script type="text/javascript" src="/cache/en/rsi-external-js.js?v=9.185.0"></script>
<script type="text/javascript" src="/cache/en/rsi-templates-js.js?v=9.185.0"></script>

        
          
<link rel="stylesheet" href="https://use.typekit.net/dhw3beb.css">



          
<script type="text/javascript" src='/rsi/static/packages/core/rsi.core.build.e8130.js'></script>
<script type="text/javascript" src='/rsi/static/packages/account/rsi.account.build.74772.js'></script>
<script type="text/javascript" src='/rsi/static/packages/store/rsi.store.build.0278b.js'></script>

<script>
                
    $(document).ready(function() {
    window.Common = new RSI.Common({});
    window.Main = new RSI.Main({
        'is_mobile': 0,
        'probation_cookie' : '',
        'require_captcha': 0
    });
    window.Mark = new Turbulent.Mark({ 'name' : 'Rsi-XSRF', 'token' : 'p5ETaA:ONCnlJtjcuYxEaE4IcmF7Q', 'ttl' : 1800 });

    window.WscOverlay = new RSI.WscOverlay({});

    var destinations = [];

window.Main.destinations = destinations;    
    
    
    });

    $(window).load(function() {
    
    });
</script>


    <script>
    window.recaptcha_is_loaded = false;
    window.on_recaptcha_load_callback = function() {
    window.recaptcha_is_loaded = true;
    };
</script>

<script
    src="https://www.recaptcha.net/recaptcha/enterprise.js?onload=on_recaptcha_load_callback&render=6LerBOgUAAAAAKPg6vsAFPTN66Woz-jBClxdQU-o"
    async defer>
</script>
    <script type="text/javascript">
      
    </script>

    

    
  <style>
    
      background:url(https://cdn.robertsspaceindustries.com/static/images/noisebg.gif) repeat center top #000b11;
    
  </style>

    <link href="https://robertsspaceindustries.com/rsi/assets/fonts.css?family=Electrolize|Orbitron:400,500,700|Quantico|Share+Tech+Mono" rel="stylesheet" type="text/css">

    <link href="/cache/en/rsi-css.css?v=9.185.0" media="all" rel="stylesheet">


    <script 
    type="module" 
    data-cookieconsent="ignore" 
    src="https://robertsspaceindustries.com/plt-client/plt-client.es.js"
    data-platform-client-props="{&quot;lang&quot;:&quot;en&quot;,&quot;user&quot;:{&quot;isSignedIn&quot;:true,&quot;avatar&quot;:&quot;\/media\/0rixm629l5bwwr\/avatar\/A5ce2752-Ce33-446e-Ae18-2dab9f9ead8a.jpg&quot;,&quot;referral&quot;:{&quot;referralCode&quot;:&quot;STAR-73KP-54LB&quot;,&quot;referralUrl&quot;:&quot;https%3A%2F%2Frobertsspaceindustries.com%2Fenlist%3Freferral%3DSTAR-73KP-54LB&quot;,&quot;referralUrlCopy&quot;:&quot;https:\/\/robertsspaceindustries.com\/enlist?referral=STAR-73KP-54LB&quot;},&quot;useLegacyAccountPanel&quot;:false,&quot;isSubscriber&quot;:false,&quot;favorite&quot;:{&quot;img&quot;:&quot;https:\/\/media.robertsspaceindustries.com\/9qvh53v4nyx8d\/heap_thumb.png&quot;,&quot;name&quot;:&quot;Civilian&quot;},&quot;xsrfToken&quot;:{&quot;cookieName&quot;:&quot;Rsi-XSRF&quot;,&quot;token&quot;:&quot;p5ETaA:ONCnlJtjcuYxEaE4IcmF7Q&quot;,&quot;ttlMargin&quot;:1800000,&quot;cookieValue&quot;:null}}}"
></script>
  </head>

    <body id="" class=""  lang=en localized=1>
    
          

    
            
<div 
  data-rsi-component="PlatformBar.Data"
  data-rsi-component-props='{
    "root": "home",
    "active": "dyn_bd_first_level_Arrisan_Amoria",
    "api": {
      "nav": {
        "url": "/nav/",
        "load": ["main","games","shop","explore","community","support","tools"]
      }
    },
    "nodes": {
                  "dyn_bd_first_level_Arrisan_Amoria": {"slug":"dyn_bd_first_level_Arrisan_Amoria","parent":"home","item":{"title":"Arrisan_Amoria"}},
                  "home": {
        "toolbar": ["launcher-link"]
      },
            "buy-star-citizen": {
        "item": {
          "link": {
            "href": "\/download"
          }
        }
      },
      "subscribers": {"children":["subscription-become","subscribers-store"]},
      "subscribers-store": {"item":{"link":{"href":"\/store\/pledge\/browse\/extras\/subscribers-store"}}},
      "subscription": {"item":{"link":{"href":"\/pledge\/subscriptions"}}}
    },
    "layouts": {
      "store-all": null
    },
    "localeSelector": {
      "available": {
        "languages": ["en"]
      },
      "selected": {
        "language": "en"
      }
            ,"languages": {"en":{"code":"en","label":"English","codeLabel":"en","subLabel":null,"altCodes":null,"badges":[],"url":"\/en\/citizens\/Arrisan_Amoria"}}
                  ,"currency": {"USD":{"iso":"USD","symbol":"$","label":"United States dollar"},"CAD":{"iso":"CAD","symbol":"$","label":"Canadian dollar"},"EUR":{"iso":"EUR","symbol":"\u20ac","label":"Euro"},"GBP":{"iso":"GBP","symbol":"\u00a3","label":"Pound sterling"}}
          },
        "tools": {
      "launcher-link": {
        "title": "Download",
        "href": "\/download"
      }
    },
    "translations": {
      "backToRSIMobile": "BACK TO RSI.com",
      "cancelButton": "Cancel",
      "confirmButton": "Confirm",
      "currencyTitle": "Currency",
      "languageTitle": "Language"
    }
  }'>
</div>

<div
    data-rsi-component="PlatformBar.Head"
    data-rsi-component-props='{
        "breadCrumbCurrentItem": null    }'
    data-orion-skin="default"
    data-orion-theme=""
></div>

  <div
    data-rsi-component="PlatformBar.Navigation"
    data-orion-skin="default"
    data-orion-theme=""
  ></div>
    

    <div id="bodyWrapper">
            <div id="platform-client-root"></div>
      
    
  <div class="page-wrapper">
    
    <div id="contentbody" class="public-profile public-profile-landing" style="">
      
  <div id="profile" class="wrapper">
    <h1 class="page-title ">
  <span class="top-line"></span>
  <span class="inner-line"></span>
  <span class="icon"></span>CITIZEN DOSSIER
  <span class="bottom-line"></span>
</h1>    <div id="public-profile" class="account-profile">
          <div class="tabs tabs2">
        <div class="holder clearfix">
          <a href="/citizens/Arrisan_Amoria" class="holotab active">
            <span class="text trans-02s">Overview</span>
            <span class="top trans-02s"></span>
            <span class="bottom trans-02s"></span>
          </a>
          <a href="/citizens/Arrisan_Amoria/organizations" class="holotab right">
            <span class="text trans-02s">Organizations</span>
            <span class="top trans-02s"></span>
            <span class="bottom trans-02s"></span>
          </a>
        </div>
      </div>
      <div class="profile-content overview-content clearfix">
        <p class="entry citizen-record">
          <span class="label">UEE Citizen Record</span>
          <strong class="value">#2106125</strong>
        </p>
        <div class="box-content profile-wrapper clearfix">
          <div class="inner-bg clearfix">
            <div class="profile left-col">
              <span class="title">Profile </span>
              <div class="inner clearfix">
                <div class="thumb">
                  <img src="/media/p3xwj8r2qojzcr/heap_infobox/C9e4adb5-3d79-448a-88dd-99f9dd598ae0.png" />
                  <span class="deco-corner top left"></span>
                  <span class="deco-corner top right"></span>
                  <span class="deco-corner bottom left"></span>
                  <span class="deco-corner bottom right"></span>
                </div>
                <div class="info">
                  <p class="entry">
                    <strong class="value">Arrisan Amoria</strong>
                  </p>
                  <p class="entry">
                    <span class="label">Handle name</span>
                    <strong class="value">Arrisan_Amoria</strong>
                  </p>
                                      <p class="entry">
                                              <span class="icon">
                          <img src="https://media.robertsspaceindustries.com/mo4h1ktyopbe3/heap_thumb.png"/>
                        </span>
                                            <span class="value">Vice Admiral</span>
                    </p>
                                  </div>
              </div>
            </div>
            <div class="main-org right-col visibility-">
              <span class="title">Main organization </span>
              <div class="inner clearfix">
                                  <div class="empty">NO MAIN ORG FOUND IN PUBLIC RECORDS</div>
                              </div>
              <span class="deco-separator top"></span>
              <span class="deco-separator bottom"></span>
                          </div>
          </div>
          <span class="deco-corner top left"></span>
          <span class="deco-corner top right"></span>
          <span class="deco-corner bottom left"></span>
          <span class="deco-corner bottom right"></span>
          <span class="deco-edge left"><span class="top"></span><span class="bottom"></span></span>
          <span class="deco-edge right"><span class="top"></span><span class="bottom"></span></span>
        </div>
        <div class="left-col">
          <div class="inner">
            <p class="entry">
              <span class="label">Enlisted</span>
              <strong class="value">Oct 15, 2018</strong>
            </p>
                          <p class="entry">
                <span class="label">Location</span>
                <strong class="value">
                  France
                                      , Bretagne
                                  </strong>
              </p>
                        <p class="entry">
              <span class="label">Fluency</span>
              <strong class="value">                                                  French,                                  English                                </strong>
            </p>
          </div>
        </div>
        <div class="right-col">
          <div class="inner">
                                                            </div>
        </div>
              </div>
    </div>
  </div>

    </div>
    
  </div>

  



               <script id="tpl_number_counter_digits" type="text/x-jsmart-tmpl">{if !$seperator}{$seperator=','}{/if}
{if !$first_max}{$first_max=9}{/if}
{for $digit = 0 to $length-1}
  <div class="mask">
    <div class="carousel">
      {if $digit == 0}
        {$max = $first_max}
      {else}
        {$max = 9}
      {/if}
      {for $i=0 to $max}
        <div class="item {if $val_arr[$digit] == $i}on{/if}" rel="{$i}">{$i}</div>
      {/for}
    </div>
  </div>
  {if ($length - $digit) % 3 == 1 && $digit != $length-1}
  <div class="seperator">{$seperator}</div>
  {/if}
{/for}</script>
<script id="base_modal" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
  <div class="top-border">
    {block name="modal_lines"}
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    {/block}
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
  </div>
  <div class="modal-inner">
    <a class="close js-close trans-03s .trans-opacity" href=""></a>
    {block name="modal_content"}{/block}
    {block name="modal_footer"}{/block}
  </div>
  <div class="bottom-border">
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
    {block name="modal_lines"}
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    {/block}
  </div>
</div></script>
<script id="base_modal_flat" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
  
  <div class="modal-inner">
    <a class="close js-close trans-03s .trans-opacity" href=""></a>
    {block name="modal_content"}{/block}
    {block name="modal_footer"}{/block}
  </div>
  
</div></script>
<script id="tpl_modals_slideshow" type="text/x-jsmart-tmpl"><img class="top-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_top.png">
<a href="" class="close js-close"></a>
<div class="mask">
  <a class="js-prev prev control"></a>
  <a class="js-next next control"></a>
  <div class="slideshow-carousel carousel" rel="{$index}">
    {foreach from=$images item="image"}
      <div class="{if $index == $image@index}on{/if}">
      {if $image.is_video}
        <div class="video-holder">
          <div id="slideshow_video_{$image@index}" data-source="{$image->source_url}">
            <video width="100%" height="100%" preload="auto" {if $video}src="{$image->source_url}"{/if} controls></video>
          </div>
        </div>
      {else}
        <div class="media js-media-slideshow-{$image@iteration}">
        {if $image.low_res}
          <picture>
            <!--[if IE 9]><video style="display: none;"><![endif]-->
            <source data-srcset="{$image.full_res}" media="(min-width: 300px)" />
            <!--[if IE 9]></video><![endif]-->
            <img data-srcset="{$image.low_res}" alt="{$image.title}" />
          </picture>
        {else}
          <img data-src="{$image.source_url}" />
        {/if}
        </div>
      {/if}
        <div class="text">
          {if !$image.is_video}
          <a href="{$image.source_url}" class="download"></a>
          {/if}
          <div class="copyright">© 2012-{$year}<br />Cloud Imperium Games Corporation &<br />Roberts Space Industries Corp.</div>
          <div class="page-number">{$image@iteration} / {count($images)}</div>
          <div class="caption v-center">{if $image.title && $image.title != "undefined"}{$image.title}{/if}</div>
          <div class="cboth"></div>
        </div>
      </div>
    {/foreach}
  </div>
</div>
<img class="bottom-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_bottom.png"></script>
<script id="tpl_contact_us" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
  <div class="top-border">
    
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
  </div>
  <div class="modal-inner">
    <a class="close js-close trans-03s .trans-opacity" href=""></a>
    
<div id="contact" class="inner-content on">
  <h2><span class="icon"></span>CONTACT</h2>
  <div class="padder">
    <div class="separator"></div>
    <form name="" action="" method="POST" class="legacy-form">
  <div class="error-message js-error-message"></div>
  <div class="success-message js-success-message"></div>
    <fieldset>
    <label for="contact_subject">Subject</label>
    <input type="text" name="subject" value="" class="trans-02s trans-color trans-box-shadow" id="contact_subject" />
    <label>Contacting us for:</label>
    <ul class="category-info">
            <li id="tech_support_info">Questions about download, installation, networking, or in-game client problems</li>
            <li id="subscription_info">Questions about monthly and yearly subscription plans</li>
            <li id="account_billing_info">Issues related to your account, such as incorrect information or ability to access account, or Billing with regards to payments and payment methods</li>
            <li id="melt_request_info">To reclaim a pledge over $1,000 for store credit (please note - this is a permanent action)</li>
            <li id="merchandise_info">Questions about physical and/or shipped merchandise</li>
            <li id="hacked_info">Issues related to compromised account or missing pledge.</li>
            <li id="account_recovery_info">For issues with account authentication, lost passwords and related queries</li>
            <li id="probation_info">Issues related to forums probation or ban</li>
            <li id="refund_request_info">Refund requests and related inquiries</li>
            <li id="customer_support_info">For general questions and queries regarding Star Citizen</li>
          </ul>
  </fieldset>
  <fieldset>
    <label for="contact_text">Description</label>
    <textarea name="text" class="trans-02s trans-color trans-box-shadow" id="contact_text"></textarea>
  </fieldset>
  <div class="contact-submit-wrapper">
    <div class="line"></div>
    <button class="submit js-submit"><strong>submit your message</strong></button>
  </div>
</form>
    <div class="separator"></div>
  </div>
</div>

    
  </div>
  <div class="bottom-border">
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
    
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    
  </div>
</div></script>
<script id="tpl_error" type="text/x-jsmart-tmpl"><div class="modal-error js-modal-error">
  <p class="modal-text js-modal-text"></p>
  <a class="close js-close trans-03s .trans-opacity" href=""></a>
</div></script>
<script id="tpl_success" type="text/x-jsmart-tmpl"><div class="modal-success js-modal-success">
  <p class="modal-text js-modal-text"></p>
  <a class="close js-close trans-03s .trans-opacity" href=""></a>
</div></script>
<script id="tpl_progress" type="text/x-jsmart-tmpl"><div class="modal-progress js-modal-progress">
  <div class="traj-loader">
    <div class="fast-blink"></div>
    <span class="modal-text js-modal-text"></span>
  </div>
</div></script>
<script id="tpl_outbound" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
  <div class="top-border">
    
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
  </div>
  <div class="modal-inner">
    <a class="close js-close trans-03s .trans-opacity" href=""></a>
    
<div id="outbound" class="inner-content on">
  <h2><span class="icon"></span>OUTBOUND LINK</h2>
  <div class="padder">
    <div class="separator"></div>
    <form name="" action="" method="POST" class="legacy-form">
      <div class="error-message js-error-message"> <span class=important>WARNING</span><br/><br/> This link will bring you outside of the RSI site and into the depths of the internet. Continue?<br/><br/><span class="url"></span> </div>
      <div class="success-message js-success-message"><span class=important>STAND BY</span><br/><br/> Initiating hyperlink.<br/><br/></div>

      <fieldset class="clearfix last">
        <span class="submit-wrapper">
          <span class="submit-hover trans-02s trans-opacity"></span>
          <input type="submit" value="WARP" class="trans-02s trans-color trans-background" />
        </span>
      </fieldset>
    </form>
    <div class="separator"></div>
  </div>
</div>

    
  </div>
  <div class="bottom-border">
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
    
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    
  </div>
</div></script>

<script id="tpl_l-notification-bar" type="text/x-jsmart-tmpl"><div class="l-notification-bar js-notification-bar">

  <div class="l-notification-bar__watermark js-svg-inliner h-svg__logo-star-citizen"></div>

  <div class="l-notification-bar__boxes">
    {if !$viewedCookieNotif}
      <div class="l-notification-bar__box">
        {include file='tpl_c-notification'
          type='cookie'
          title='COOKIES:'
          message="Our website uses Google Analytics to analyze our traffic. <br/>To learn how you can control Google's use of your data and how you can opt out <a href='https://www.google.com/policies/privacy/partners/'>click here</a>."
          linkText='See Details'
          buttonText='Got it!'}
      </div>
    {/if}

    {if !$viewedPrivacyNotif}
      <div class="l-notification-bar__box">
        {include file='tpl_c-notification'
          type='privacy'
          title='PRIVACY POLICY:'
          message='We adjusted the PP to reflect the decision of the European Court of Justice regarding Safe Harbor, the fact that RSI has moved and added some services providers.'
          linkText='View Privacy Policy'
          buttonText='Got it!'}
      </div>
    {/if}
  </div>

</div>
</script>
<script id="tpl_c-notification" type="text/x-jsmart-tmpl"><div class="c-notification js-bottom-notif-msg-{$type}">
    <div class="c-notification__title">{$title}</div>
    <div class="c-notification__message">
      {$message}
    </div>

    {if $linkText}
        <div class="c-notification__wrapper-link">
            <a class="c-notification__link js-bottom-notif-link-{$type}">
            {$linkText}
            </a>
        </div>
    {/if}

    <a class="c-notification__button js-bottom-notif-btn-{$type}">

      <span class="c-notification__button-text">
       {$buttonText}
      </span>

      {if $type neq 'announcement'}
        <div class="c-iconed__icon c-iconed__icon--checkmark"></div>
      {/if}
    </a>
</div>
</script>

<script id="tpl_confirm" type="text/x-jsmart-tmpl"><div class="modal-confirm js-modal-confirm clearfix">
  <p class="modal-text js-modal-text"></p>
  <a class="bt-close js-close trans-03s trans-opacity" href=""></a>
  <a class="bt-confirm js-confirm trans-03s trans-opacity" href=""></a>
	<div class="buttons">
		<a class="shadow-button trans-02s trans-color js-close bt-close rm"     >
  <span class="label js-label trans-02s">Cancel</span>
  <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
  <span class="left-section"></span>
  <span class="right-section"></span>
</a>
		<a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
  <span class="label js-label trans-02s">Confirm</span>
  <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
  <span class="left-section"></span>
  <span class="right-section"></span>
</a>
	</div>
</div>
</script>
<script id="tpl_alert" type="text/x-jsmart-tmpl"><div class="modal-alert js-modal-alert clearfix">
  <p class="modal-text js-modal-text"></p>
  <div class="buttons">
    <a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
  <span class="label js-label trans-02s">OK</span>
  <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
  <span class="left-section"></span>
  <span class="right-section"></span>
</a>
  </div>
</div></script>
<script id="tpl_video" type="text/x-jsmart-tmpl">{extends file="base_modal"}
{block name='modal_content'}
<div id="ship-commercial" class="inner-content">

  <div class="hr"></div>
  <div class="content-block4">

    <div class="bottom"></div>
  </div>
  {if $distant_source=="vimeo"}
  <iframe id="commercial" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="//player.vimeo.com/video/{$video_id}?wmode=transparent" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>
  {else}
  <iframe id="commercial" frameborder="0" allowfullscreen="1" title="YouTube video player" width="100%" height="100%" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="https://www.youtube.com/embed/{$video_id}?autoplay=1"></iframe>
  {/if}
</div>
{/block}
</script>
      

      
        
    

<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KHNFZPT"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->


<div data-rsi-component="PlatformFooter" data-rsi-component-props='{
  "currentSection": "rsi",
  "wscAbout": "/star-citizen",
  "wscPlay": "/playstarcitizen",
  "s42Game": "/squadron42",
  "s42Enlist": "/squadron42#enlist",
  "rsiCommlink": "/comm-link",
  "rsiCommunity": "/community-hub",
  "rsiRoadmap": "/roadmap",
  "showStoreMenu": "1",
  "isStoreMenuActive": "",
  "rsiStore": "/pledge",
  "rsiDownload": "/download",
  "isLauncherMenuActive": "",
  "rsiSpectrum": "/spectrum/community/SC",
  "showCitizenconMenu": "1",
  "rsiCitizencon": "/citizencon",
  "utilitiesHelp": "//support.robertsspaceindustries.com",
  "utilitiesPress": "/press",
  "utilitiesCareers": "https://cloudimperiumgames.com/join-us",
  "utilitiesAcknowledgement": "/acknowledgements",
  "utilitiesRedeemCode": "/pledge/redeem-code",
  "legalLegal": "/legal",
  "legalTos": "/tos",
  "legalPrivacy": "/privacy",
  "legalEula": "/eula",
  "legalDmca": "/dmca",
  "legalDisclosure": "/responsible-disclosure",
  "legalCaliforniaLegalNoticeAtCollection": "/privacy#california",
  "legalCaliforniaLegalPersonalInformation": "/cookies#preferences",
  "isConsentRequired": "",
  "clientRecordCountry": "GB",
  "cigLink": "https://cloudimperiumgames.com",
  "displayStarEngine": ""
}'></div>
      
    </div>
  </body>
</html>

    """

@pytest.fixture
def pilot_with_weird_long_org_name():
    #  https://robertsspaceindustries.com/en/citizens/Nazgoroth
    return """
    
<!DOCTYPE html>
    
<html lang="en">
  <head>
        
    <script
    id="TagManager"
    data-cookieconsent="ignore"
    data-app-name="rsi-heap"
    data-app-version="9.185.0"
    data-category="account"
    data-sub-category="account-profile-public"
    src="/tag-manager/script.js"
    type="text/javascript"></script>
        <script
    type="text/javascript"
    id="Cookiebot"
    src="https://consent.cookiebot.com/uc.js"
    data-cbid="a687ee30-df65-45a0-9d22-90de6c1bb964"
    data-blockingmode="auto"
    data-georegions="{'region':'US-06,US-51,AT,BE,BG,HR,CY,CZ,DK,EE,FI,FR,DE,GR,HU,IE,IT,LV,LT,LU,MT,NL,PL,PT,RO,SK,SL,ES,SE','cbid':'a687ee30-df65-45a0-9d22-90de6c1bb964'}"></script>
    <script id="CookieConsent" src="/cookie-consent/script.js?async=false" type="text/javascript"></script>
  <link href="/rsi/static/css/cookiebot.css?v=9.185.0" rel="stylesheet" />
        <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
    <meta name="description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans.">

    <meta name="csrf-token" content="9de548adfd3c7270d237683ea4ea2b174d51689a95e7352bb2325fd5bdabc7df" />
    <meta property="og:site_name" content="
Nazgoroth | Nazgoroth - Vanguard &equiv;\ /&equiv; | VNGD (Chief) - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
" />
    <meta property="og:image" content="https://cdn.robertsspaceindustries.com/static/images/RSI-fb.jpg" />
    <meta property="og:description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans." />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://robertsspaceindustries.com/en/citizens/Nazgoroth" />
    <meta property="og:locale" content="en" />

    <title>
Nazgoroth | Nazgoroth - Vanguard &equiv;\ /&equiv; | VNGD (Chief) - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
</title>

    <link rel="canonical" href="https://robertsspaceindustries.com/en/citizens/Nazgoroth">

    
                  <link rel="alternate" href="https://robertsspaceindustries.com/en/citizens/Nazgoroth" hreflang="en">
                            

        <link rel=preconnect href="//sentry.turbulent.ca">
    <link rel=preconnect href="//gstatic.com">
    <link rel=preconnect href="//www.recaptcha.net">
    <link rel=preconnect href="//www.googletagmanager.com">
      

        <link href="/rsi/static/css/rsi-minimal.css?v=9.185.0" media="all" rel="stylesheet">
    
<link href="/rsi/static/css/cross-brand-less.css?v=9.185.0" media="all" rel="stylesheet">


          
<script type="text/javascript" src="/cache/en/rsi-external-js.js?v=9.185.0"></script>
<script type="text/javascript" src="/cache/en/rsi-templates-js.js?v=9.185.0"></script>

        
          
<link rel="stylesheet" href="https://use.typekit.net/dhw3beb.css">



          
<script type="text/javascript" src='/rsi/static/packages/core/rsi.core.build.e8130.js'></script>
<script type="text/javascript" src='/rsi/static/packages/account/rsi.account.build.74772.js'></script>
<script type="text/javascript" src='/rsi/static/packages/store/rsi.store.build.0278b.js'></script>

<script>
                
    $(document).ready(function() {
    window.Common = new RSI.Common({});
    window.Main = new RSI.Main({
        'is_mobile': 0,
        'probation_cookie' : '',
        'require_captcha': 0
    });
    window.Mark = new Turbulent.Mark({ 'name' : 'Rsi-XSRF', 'token' : 'uacTaA:1RWuDoab+3zbFtIG4EwIJA', 'ttl' : 1800 });

    window.WscOverlay = new RSI.WscOverlay({});

    var destinations = [];

window.Main.destinations = destinations;    
    
    
    });

    $(window).load(function() {
    
    });
</script>


    <script>
    window.recaptcha_is_loaded = false;
    window.on_recaptcha_load_callback = function() {
    window.recaptcha_is_loaded = true;
    };
</script>

<script
    src="https://www.recaptcha.net/recaptcha/enterprise.js?onload=on_recaptcha_load_callback&render=6LerBOgUAAAAAKPg6vsAFPTN66Woz-jBClxdQU-o"
    async defer>
</script>
    <script type="text/javascript">
      
    </script>

    

    
  <style>
    
      background:url(https://cdn.robertsspaceindustries.com/static/images/noisebg.gif) repeat center top #000b11;
    
  </style>

    <link href="https://robertsspaceindustries.com/rsi/assets/fonts.css?family=Electrolize|Orbitron:400,500,700|Quantico|Share+Tech+Mono" rel="stylesheet" type="text/css">

    <link href="/cache/en/rsi-css.css?v=9.185.0" media="all" rel="stylesheet">


    <script 
    type="module" 
    data-cookieconsent="ignore" 
    src="https://robertsspaceindustries.com/plt-client/plt-client.es.js"
    data-platform-client-props="{&quot;lang&quot;:&quot;en&quot;,&quot;user&quot;:{&quot;isSignedIn&quot;:true,&quot;avatar&quot;:&quot;\/media\/0rixm629l5bwwr\/avatar\/A5ce2752-Ce33-446e-Ae18-2dab9f9ead8a.jpg&quot;,&quot;referral&quot;:{&quot;referralCode&quot;:&quot;STAR-73KP-54LB&quot;,&quot;referralUrl&quot;:&quot;https%3A%2F%2Frobertsspaceindustries.com%2Fenlist%3Freferral%3DSTAR-73KP-54LB&quot;,&quot;referralUrlCopy&quot;:&quot;https:\/\/robertsspaceindustries.com\/enlist?referral=STAR-73KP-54LB&quot;},&quot;useLegacyAccountPanel&quot;:false,&quot;isSubscriber&quot;:false,&quot;favorite&quot;:{&quot;img&quot;:&quot;https:\/\/media.robertsspaceindustries.com\/9qvh53v4nyx8d\/heap_thumb.png&quot;,&quot;name&quot;:&quot;Civilian&quot;},&quot;xsrfToken&quot;:{&quot;cookieName&quot;:&quot;Rsi-XSRF&quot;,&quot;token&quot;:&quot;uacTaA:1RWuDoab+3zbFtIG4EwIJA&quot;,&quot;ttlMargin&quot;:1800000,&quot;cookieValue&quot;:null}}}"
></script>
  </head>

    <body id="" class=""  lang=en localized=1>
    
          

    
            
<div 
  data-rsi-component="PlatformBar.Data"
  data-rsi-component-props='{
    "root": "home",
    "active": "dyn_bd_first_level_Nazgoroth",
    "api": {
      "nav": {
        "url": "/nav/",
        "load": ["main","games","shop","explore","community","support","tools"]
      }
    },
    "nodes": {
                  "dyn_bd_first_level_Nazgoroth": {"slug":"dyn_bd_first_level_Nazgoroth","parent":"home","item":{"title":"Nazgoroth"}},
                  "home": {
        "toolbar": ["launcher-link"]
      },
            "buy-star-citizen": {
        "item": {
          "link": {
            "href": "\/download"
          }
        }
      },
      "subscribers": {"children":["subscription-become","subscribers-store"]},
      "subscribers-store": {"item":{"link":{"href":"\/store\/pledge\/browse\/extras\/subscribers-store"}}},
      "subscription": {"item":{"link":{"href":"\/pledge\/subscriptions"}}}
    },
    "layouts": {
      "store-all": null
    },
    "localeSelector": {
      "available": {
        "languages": ["en"]
      },
      "selected": {
        "language": "en"
      }
            ,"languages": {"en":{"code":"en","label":"English","codeLabel":"en","subLabel":null,"altCodes":null,"badges":[],"url":"\/en\/citizens\/Nazgoroth"}}
                  ,"currency": {"USD":{"iso":"USD","symbol":"$","label":"United States dollar"},"CAD":{"iso":"CAD","symbol":"$","label":"Canadian dollar"},"EUR":{"iso":"EUR","symbol":"\u20ac","label":"Euro"},"GBP":{"iso":"GBP","symbol":"\u00a3","label":"Pound sterling"}}
          },
        "tools": {
      "launcher-link": {
        "title": "Download",
        "href": "\/download"
      }
    },
    "translations": {
      "backToRSIMobile": "BACK TO RSI.com",
      "cancelButton": "Cancel",
      "confirmButton": "Confirm",
      "currencyTitle": "Currency",
      "languageTitle": "Language"
    }
  }'>
</div>

<div
    data-rsi-component="PlatformBar.Head"
    data-rsi-component-props='{
        "breadCrumbCurrentItem": null    }'
    data-orion-skin="default"
    data-orion-theme=""
></div>

  <div
    data-rsi-component="PlatformBar.Navigation"
    data-orion-skin="default"
    data-orion-theme=""
  ></div>
    

    <div id="bodyWrapper">
            <div id="platform-client-root"></div>
      
    
  <div class="page-wrapper">
    
    <div id="contentbody" class="public-profile public-profile-landing" style="">
      
  <div id="profile" class="wrapper">
    <h1 class="page-title ">
  <span class="top-line"></span>
  <span class="inner-line"></span>
  <span class="icon"></span>CITIZEN DOSSIER
  <span class="bottom-line"></span>
</h1>    <div id="public-profile" class="account-profile">
          <div class="tabs tabs2">
        <div class="holder clearfix">
          <a href="/citizens/Nazgoroth" class="holotab active">
            <span class="text trans-02s">Overview</span>
            <span class="top trans-02s"></span>
            <span class="bottom trans-02s"></span>
          </a>
          <a href="/citizens/Nazgoroth/organizations" class="holotab right">
            <span class="text trans-02s">Organizations</span>
            <span class="top trans-02s"></span>
            <span class="bottom trans-02s"></span>
          </a>
        </div>
      </div>
      <div class="profile-content overview-content clearfix">
        <p class="entry citizen-record">
          <span class="label">UEE Citizen Record</span>
          <strong class="value">n/a</strong>
        </p>
        <div class="box-content profile-wrapper clearfix">
          <div class="inner-bg clearfix">
            <div class="profile left-col">
              <span class="title">Profile </span>
              <div class="inner clearfix">
                <div class="thumb">
                  <img src="/media/mdd322lttggxer/heap_infobox/C6d8eec7-9b0d-401e-B1de-05524a36c01f.png" />
                  <span class="deco-corner top left"></span>
                  <span class="deco-corner top right"></span>
                  <span class="deco-corner bottom left"></span>
                  <span class="deco-corner bottom right"></span>
                </div>
                <div class="info">
                  <p class="entry">
                    <strong class="value">Nazgoroth</strong>
                  </p>
                  <p class="entry">
                    <span class="label">Handle name</span>
                    <strong class="value">Nazgoroth</strong>
                  </p>
                                      <p class="entry">
                                              <span class="icon">
                          <img src="https://media.robertsspaceindustries.com/nbknae4i2vllg/heap_thumb.png"/>
                        </span>
                                            <span class="value">2953 Master-At-Arms</span>
                    </p>
                                  </div>
              </div>
            </div>
            <div class="main-org right-col visibility-V">
              <span class="title">Main organization </span>
              <div class="inner clearfix">
                                  <div class="thumb">
                                                                                  <a href="/orgs/VNGD"><img src="/media/jh3aq5aeu8qa7r/heap_infobox/VNGD-Logo.png" /></a>
                                        <span class="deco-corner top left"></span>
                    <span class="deco-corner top right"></span>
                    <span class="deco-corner bottom left"></span>
                    <span class="deco-corner bottom right"></span>
                  </div>
                  <div class="info">
                    <p class="entry">
                                            <a href="/orgs/VNGD" class="value data12" style="background-position:-249px center">Vanguard &equiv;\ /&equiv;</a>
                    </p>
                    <p class="entry">
                                            <span class="label data7">Spectrum Identification (SID)</span>
                                            <strong class="value data10">VNGD</strong>
                    </p>
                    <p class="entry">
                                            <span class="label data4">Organization rank</span>
                                            <strong class="value data11">Chief</strong>
                    </p>
                    <div class="ranking data11">
                                                                        <span class="active"><span></span></span>
                                                  <span class="active"><span></span></span>
                                                  <span ><span></span></span>
                                                  <span ><span></span></span>
                                                  <span ><span></span></span>
                                                                  </div>
                  </div>
                              </div>
              <span class="deco-separator top"></span>
              <span class="deco-separator bottom"></span>
                          </div>
          </div>
          <span class="deco-corner top left"></span>
          <span class="deco-corner top right"></span>
          <span class="deco-corner bottom left"></span>
          <span class="deco-corner bottom right"></span>
          <span class="deco-edge left"><span class="top"></span><span class="bottom"></span></span>
          <span class="deco-edge right"><span class="top"></span><span class="bottom"></span></span>
        </div>
        <div class="left-col">
          <div class="inner">
            <p class="entry">
              <span class="label">Enlisted</span>
              <strong class="value">Sep 17, 2021</strong>
            </p>
                        <p class="entry">
              <span class="label">Fluency</span>
              <strong class="value">                                                  Dutch,                                  English                                </strong>
            </p>
          </div>
        </div>
        <div class="right-col">
          <div class="inner">
                                                    <div class="entry bio">
                <span class="label">Bio</span>
                <div class="value">
                  The Ambassador.
                </div>
              </div>
                                    </div>
        </div>
              </div>
    </div>
  </div>

    </div>
    
  </div>

  



               <script id="tpl_number_counter_digits" type="text/x-jsmart-tmpl">{if !$seperator}{$seperator=','}{/if}
{if !$first_max}{$first_max=9}{/if}
{for $digit = 0 to $length-1}
  <div class="mask">
    <div class="carousel">
      {if $digit == 0}
        {$max = $first_max}
      {else}
        {$max = 9}
      {/if}
      {for $i=0 to $max}
        <div class="item {if $val_arr[$digit] == $i}on{/if}" rel="{$i}">{$i}</div>
      {/for}
    </div>
  </div>
  {if ($length - $digit) % 3 == 1 && $digit != $length-1}
  <div class="seperator">{$seperator}</div>
  {/if}
{/for}</script>
<script id="base_modal" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
  <div class="top-border">
    {block name="modal_lines"}
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    {/block}
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
  </div>
  <div class="modal-inner">
    <a class="close js-close trans-03s .trans-opacity" href=""></a>
    {block name="modal_content"}{/block}
    {block name="modal_footer"}{/block}
  </div>
  <div class="bottom-border">
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
    {block name="modal_lines"}
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    {/block}
  </div>
</div></script>
<script id="base_modal_flat" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
  
  <div class="modal-inner">
    <a class="close js-close trans-03s .trans-opacity" href=""></a>
    {block name="modal_content"}{/block}
    {block name="modal_footer"}{/block}
  </div>
  
</div></script>
<script id="tpl_modals_slideshow" type="text/x-jsmart-tmpl"><img class="top-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_top.png">
<a href="" class="close js-close"></a>
<div class="mask">
  <a class="js-prev prev control"></a>
  <a class="js-next next control"></a>
  <div class="slideshow-carousel carousel" rel="{$index}">
    {foreach from=$images item="image"}
      <div class="{if $index == $image@index}on{/if}">
      {if $image.is_video}
        <div class="video-holder">
          <div id="slideshow_video_{$image@index}" data-source="{$image->source_url}">
            <video width="100%" height="100%" preload="auto" {if $video}src="{$image->source_url}"{/if} controls></video>
          </div>
        </div>
      {else}
        <div class="media js-media-slideshow-{$image@iteration}">
        {if $image.low_res}
          <picture>
            <!--[if IE 9]><video style="display: none;"><![endif]-->
            <source data-srcset="{$image.full_res}" media="(min-width: 300px)" />
            <!--[if IE 9]></video><![endif]-->
            <img data-srcset="{$image.low_res}" alt="{$image.title}" />
          </picture>
        {else}
          <img data-src="{$image.source_url}" />
        {/if}
        </div>
      {/if}
        <div class="text">
          {if !$image.is_video}
          <a href="{$image.source_url}" class="download"></a>
          {/if}
          <div class="copyright">© 2012-{$year}<br />Cloud Imperium Games Corporation &<br />Roberts Space Industries Corp.</div>
          <div class="page-number">{$image@iteration} / {count($images)}</div>
          <div class="caption v-center">{if $image.title && $image.title != "undefined"}{$image.title}{/if}</div>
          <div class="cboth"></div>
        </div>
      </div>
    {/foreach}
  </div>
</div>
<img class="bottom-border" src="https://cdn.robertsspaceindustries.com/static/images/modal_bottom.png"></script>
<script id="tpl_contact_us" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
  <div class="top-border">
    
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
  </div>
  <div class="modal-inner">
    <a class="close js-close trans-03s .trans-opacity" href=""></a>
    
<div id="contact" class="inner-content on">
  <h2><span class="icon"></span>CONTACT</h2>
  <div class="padder">
    <div class="separator"></div>
    <form name="" action="" method="POST" class="legacy-form">
  <div class="error-message js-error-message"></div>
  <div class="success-message js-success-message"></div>
    <fieldset>
    <label for="contact_subject">Subject</label>
    <input type="text" name="subject" value="" class="trans-02s trans-color trans-box-shadow" id="contact_subject" />
    <label>Contacting us for:</label>
    <ul class="category-info">
            <li id="tech_support_info">Questions about download, installation, networking, or in-game client problems</li>
            <li id="subscription_info">Questions about monthly and yearly subscription plans</li>
            <li id="account_billing_info">Issues related to your account, such as incorrect information or ability to access account, or Billing with regards to payments and payment methods</li>
            <li id="melt_request_info">To reclaim a pledge over $1,000 for store credit (please note - this is a permanent action)</li>
            <li id="merchandise_info">Questions about physical and/or shipped merchandise</li>
            <li id="hacked_info">Issues related to compromised account or missing pledge.</li>
            <li id="account_recovery_info">For issues with account authentication, lost passwords and related queries</li>
            <li id="probation_info">Issues related to forums probation or ban</li>
            <li id="refund_request_info">Refund requests and related inquiries</li>
            <li id="customer_support_info">For general questions and queries regarding Star Citizen</li>
          </ul>
  </fieldset>
  <fieldset>
    <label for="contact_text">Description</label>
    <textarea name="text" class="trans-02s trans-color trans-box-shadow" id="contact_text"></textarea>
  </fieldset>
  <div class="contact-submit-wrapper">
    <div class="line"></div>
    <button class="submit js-submit"><strong>submit your message</strong></button>
  </div>
</form>
    <div class="separator"></div>
  </div>
</div>

    
  </div>
  <div class="bottom-border">
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
    
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    
  </div>
</div></script>
<script id="tpl_error" type="text/x-jsmart-tmpl"><div class="modal-error js-modal-error">
  <p class="modal-text js-modal-text"></p>
  <a class="close js-close trans-03s .trans-opacity" href=""></a>
</div></script>
<script id="tpl_success" type="text/x-jsmart-tmpl"><div class="modal-success js-modal-success">
  <p class="modal-text js-modal-text"></p>
  <a class="close js-close trans-03s .trans-opacity" href=""></a>
</div></script>
<script id="tpl_progress" type="text/x-jsmart-tmpl"><div class="modal-progress js-modal-progress">
  <div class="traj-loader">
    <div class="fast-blink"></div>
    <span class="modal-text js-modal-text"></span>
  </div>
</div></script>
<script id="tpl_outbound" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
  <div class="top-border">
    
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
  </div>
  <div class="modal-inner">
    <a class="close js-close trans-03s .trans-opacity" href=""></a>
    
<div id="outbound" class="inner-content on">
  <h2><span class="icon"></span>OUTBOUND LINK</h2>
  <div class="padder">
    <div class="separator"></div>
    <form name="" action="" method="POST" class="legacy-form">
      <div class="error-message js-error-message"> <span class=important>WARNING</span><br/><br/> This link will bring you outside of the RSI site and into the depths of the internet. Continue?<br/><br/><span class="url"></span> </div>
      <div class="success-message js-success-message"><span class=important>STAND BY</span><br/><br/> Initiating hyperlink.<br/><br/></div>

      <fieldset class="clearfix last">
        <span class="submit-wrapper">
          <span class="submit-hover trans-02s trans-opacity"></span>
          <input type="submit" value="WARP" class="trans-02s trans-color trans-background" />
        </span>
      </fieldset>
    </form>
    <div class="separator"></div>
  </div>
</div>

    
  </div>
  <div class="bottom-border">
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
    
    <img src="https://cdn.robertsspaceindustries.com/static/images/modal_blue_line.png" />
    
  </div>
</div></script>

<script id="tpl_l-notification-bar" type="text/x-jsmart-tmpl"><div class="l-notification-bar js-notification-bar">

  <div class="l-notification-bar__watermark js-svg-inliner h-svg__logo-star-citizen"></div>

  <div class="l-notification-bar__boxes">
    {if !$viewedCookieNotif}
      <div class="l-notification-bar__box">
        {include file='tpl_c-notification'
          type='cookie'
          title='COOKIES:'
          message="Our website uses Google Analytics to analyze our traffic. <br/>To learn how you can control Google's use of your data and how you can opt out <a href='https://www.google.com/policies/privacy/partners/'>click here</a>."
          linkText='See Details'
          buttonText='Got it!'}
      </div>
    {/if}

    {if !$viewedPrivacyNotif}
      <div class="l-notification-bar__box">
        {include file='tpl_c-notification'
          type='privacy'
          title='PRIVACY POLICY:'
          message='We adjusted the PP to reflect the decision of the European Court of Justice regarding Safe Harbor, the fact that RSI has moved and added some services providers.'
          linkText='View Privacy Policy'
          buttonText='Got it!'}
      </div>
    {/if}
  </div>

</div>
</script>
<script id="tpl_c-notification" type="text/x-jsmart-tmpl"><div class="c-notification js-bottom-notif-msg-{$type}">
    <div class="c-notification__title">{$title}</div>
    <div class="c-notification__message">
      {$message}
    </div>

    {if $linkText}
        <div class="c-notification__wrapper-link">
            <a class="c-notification__link js-bottom-notif-link-{$type}">
            {$linkText}
            </a>
        </div>
    {/if}

    <a class="c-notification__button js-bottom-notif-btn-{$type}">

      <span class="c-notification__button-text">
       {$buttonText}
      </span>

      {if $type neq 'announcement'}
        <div class="c-iconed__icon c-iconed__icon--checkmark"></div>
      {/if}
    </a>
</div>
</script>

<script id="tpl_confirm" type="text/x-jsmart-tmpl"><div class="modal-confirm js-modal-confirm clearfix">
  <p class="modal-text js-modal-text"></p>
  <a class="bt-close js-close trans-03s trans-opacity" href=""></a>
  <a class="bt-confirm js-confirm trans-03s trans-opacity" href=""></a>
	<div class="buttons">
		<a class="shadow-button trans-02s trans-color js-close bt-close rm"     >
  <span class="label js-label trans-02s">Cancel</span>
  <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
  <span class="left-section"></span>
  <span class="right-section"></span>
</a>
		<a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
  <span class="label js-label trans-02s">Confirm</span>
  <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
  <span class="left-section"></span>
  <span class="right-section"></span>
</a>
	</div>
</div>
</script>
<script id="tpl_alert" type="text/x-jsmart-tmpl"><div class="modal-alert js-modal-alert clearfix">
  <p class="modal-text js-modal-text"></p>
  <div class="buttons">
    <a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
  <span class="label js-label trans-02s">OK</span>
  <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
  <span class="left-section"></span>
  <span class="right-section"></span>
</a>
  </div>
</div></script>
<script id="tpl_video" type="text/x-jsmart-tmpl">{extends file="base_modal"}
{block name='modal_content'}
<div id="ship-commercial" class="inner-content">

  <div class="hr"></div>
  <div class="content-block4">

    <div class="bottom"></div>
  </div>
  {if $distant_source=="vimeo"}
  <iframe id="commercial" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="//player.vimeo.com/video/{$video_id}?wmode=transparent" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>
  {else}
  <iframe id="commercial" frameborder="0" allowfullscreen="1" title="YouTube video player" width="100%" height="100%" src="/rsi/static/cookiebot-embed.html" data-cookieconsent="marketing" data-src="https://www.youtube.com/embed/{$video_id}?autoplay=1"></iframe>
  {/if}
</div>
{/block}
</script>
      

      
        
    

<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KHNFZPT"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->


<div data-rsi-component="PlatformFooter" data-rsi-component-props='{
  "currentSection": "rsi",
  "wscAbout": "/star-citizen",
  "wscPlay": "/playstarcitizen",
  "s42Game": "/squadron42",
  "s42Enlist": "/squadron42#enlist",
  "rsiCommlink": "/comm-link",
  "rsiCommunity": "/community-hub",
  "rsiRoadmap": "/roadmap",
  "showStoreMenu": "1",
  "isStoreMenuActive": "",
  "rsiStore": "/pledge",
  "rsiDownload": "/download",
  "isLauncherMenuActive": "",
  "rsiSpectrum": "/spectrum/community/SC",
  "showCitizenconMenu": "1",
  "rsiCitizencon": "/citizencon",
  "utilitiesHelp": "//support.robertsspaceindustries.com",
  "utilitiesPress": "/press",
  "utilitiesCareers": "https://cloudimperiumgames.com/join-us",
  "utilitiesAcknowledgement": "/acknowledgements",
  "utilitiesRedeemCode": "/pledge/redeem-code",
  "legalLegal": "/legal",
  "legalTos": "/tos",
  "legalPrivacy": "/privacy",
  "legalEula": "/eula",
  "legalDmca": "/dmca",
  "legalDisclosure": "/responsible-disclosure",
  "legalCaliforniaLegalNoticeAtCollection": "/privacy#california",
  "legalCaliforniaLegalPersonalInformation": "/cookies#preferences",
  "isConsentRequired": "",
  "clientRecordCountry": "GB",
  "cigLink": "https://cloudimperiumgames.com",
  "displayStarEngine": ""
}'></div>
      
    </div>
  </body>
</html>

    """

