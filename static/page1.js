var features = 'toolbar=no,menubar=no,location=no,scrollbars=yes,resizable=yes,status=no,left=,top=,width=,height=';
function searchPage(features)
{
   var element = document.getElementById('SiteSearch1');
   window.open('sitesearch1-results.html?q='+encodeURIComponent(element.value), '', features);
   return false;
}
function submitForm1()
{
   var regexp;
   var imguploader_productform = document.getElementById('imguploader_productform');
   var imguploader_productform_file = document.getElementById('imguploader_productform-file');
   if (!(imguploader_productform.disabled ||
         imguploader_productform.style.display === 'none' ||
         imguploader_productform.style.visibility === 'hidden'))
   {
      var ext = imguploader_productform_file.value.substr(imguploader_productform_file.value.lastIndexOf('.'));
      if ((ext.toLowerCase() != ".jpeg") &&
          (ext.toLowerCase() != ".jpg") &&
          (ext.toLowerCase() != ".png") &&
          (ext != ""))
      {
         alert("The \"imguploader_productform\" field contains an unapproved filename.");
         return false;
      }
   }
   return true;
}
$(document).ready(function()
{
   searchParseURL('SiteSearch1');
   $("#imguploader_productform :file").on('change', function()
   {
      var input = $(this).parents('.input-group').find(':text');
      input.val($(this).val());
   });
   var current_customerOpts =
   {
      delay: 0,
      duration: 500,
      easing: 'linear',
      mode: 'forward',
      direction: '',
      pagination: true,
      pagination_img_default: '../static/images/current_customer-default.png',
      pagination_img_active: '../static/images/current_customer-active.png',
      pause: null,
      start: 0
   };
   $("#current_customer").carousel(current_customerOpts);
   $("#current_customer_back a").click(function()
   {
      $('#current_customer').carousel('prev');
   });
   $("#current_customer_next a").click(function()
   {
      $('#current_customer').carousel('next');
   });
   var Carousel2Opts =
   {
      delay: 0,
      duration: 500,
      easing: 'swing',
      mode: 'slide',
      direction: 'left',
      pagination: true,
      pagination_img_default: '../static/images/Carousel2-default.png',
      pagination_img_active: '../static/images/Carousel2-active.png',
      pause: null,
      start: 0
   };
   $("#Carousel2").carouseleffects(Carousel2Opts);
   $("#Carousel2_back a").click(function()
   {
      $('#Carousel2').carouseleffects('prev');
   });
   $("#Carousel2_next a").click(function()
   {
      $('#Carousel2').carouseleffects('next');
   });
   var Carousel3Opts =
   {
      delay: 0,
      duration: 500,
      easing: 'swing',
      mode: 'slide',
      direction: 'left',
      pagination: true,
      pagination_img_default: '../static/images/Carousel3-default.png',
      pagination_img_active: '../static/images/Carousel3-active.png',
      pause: null,
      start: 0
   };
   $("#Carousel3").carouseleffects(Carousel3Opts);
   $("#Carousel3_back a").click(function()
   {
      $('#Carousel3').carouseleffects('prev');
   });
   $("#Carousel3_next a").click(function()
   {
      $('#Carousel3').carouseleffects('next');
   });
   var Carousel4Opts =
   {
      delay: 0,
      duration: 500,
      easing: 'swing',
      mode: 'slide',
      direction: 'left',
      pagination: true,
      pagination_img_default: '../static/images/Carousel4-default.png',
      pagination_img_active: '../static/images/Carousel4-active.png',
      pause: null,
      start: 0
   };
   $("#Carousel4").carouseleffects(Carousel4Opts);
   $("#Carousel4_back a").click(function()
   {
      $('#Carousel4').carouseleffects('prev');
   });
   $("#Carousel4_next a").click(function()
   {
      $('#Carousel4').carouseleffects('next');
   });
   var Carousel5Opts =
   {
      delay: 0,
      duration: 500,
      easing: 'swing',
      mode: 'slide',
      direction: 'left',
      pagination: true,
      pagination_img_default: '../static/images/Carousel5-default.png',
      pagination_img_active: '../static/images/Carousel5-active.png',
      pause: null,
      start: 0
   };
   $("#Carousel5").carouseleffects(Carousel5Opts);
   $("#Carousel5_back a").click(function()
   {
      $('#Carousel5').carouseleffects('prev');
   });
   $("#Carousel5_next a").click(function()
   {
      $('#Carousel5').carouseleffects('next');
   });
});
