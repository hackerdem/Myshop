// JavaScript Document
$(function() {
 "use strict";

  function responsive_dropdown () {
    /* ---- For Mobile Menu Dropdown JS Start ---- */
      $('#menu span.opener').on("click", function() {
        if ($(this).hasClass("plus")) {
          $(this).parent().find('.mobile-sub-menu').slideDown();
          $(this).removeClass('plus');
          $(this).addClass('minus');
        }
        else
        {
          $(this).parent().find('.mobile-sub-menu').slideUp();
          $(this).removeClass('minus');
          $(this).addClass('plus');
        }
        return false;
      });
    /* ---- For Mobile Menu Dropdown JS End ---- */

    /*---Mobile menu icon Start---*/
    var navbar_toggle = $('.navbar-toggle i');
    var menu_var = $('#menu');
    $('.navbar-toggle').on("click", function(){
      
      if(menu_var.hasClass('menu-open')){
        menu_var.removeClass('menu-open');
        navbar_toggle.removeClass('fa-close');
        navbar_toggle.addClass('fa-bars');
      }else{
        menu_var.addClass('menu-open');
        navbar_toggle.addClass('fa-close');
        navbar_toggle.removeClass('fa-bars');
      }
      return false;
    });
    /*---Mobile menu icon End---*/

    /* ---- For Sidebar JS Start ---- */
      $('.sidebar-box span.opener').on("click", function(){
      
        if ($(this).hasClass("plus")) {
          $(this).parent().find('.sidebar-contant').slideDown();
          $(this).removeClass('plus');
          $(this).addClass('minus');
        }
        else
        {
          $(this).parent().find('.sidebar-contant').slideUp();
          $(this).removeClass('minus');
          $(this).addClass('plus');
        }
        return false;
      });
    /* ---- For Sidebar JS End ---- */
    /* ---- For Footer JS Start ---- */
      $('.footer-static-block span.opener').on("click", function(){
      
        if ($(this).hasClass("plus")) {
          $(this).parent().find('.footer-block-contant').slideDown();
          $(this).removeClass('plus');
          $(this).addClass('minus');
        }
        else
        {
          $(this).parent().find('.footer-block-contant').slideUp();
          $(this).removeClass('minus');
          $(this).addClass('plus');
        }
        return false;
      });
    /* ---- For Footer JS End ---- */
  }

  function search_open () {
    /* ----- Search open close Start  ------ */
    $('.search-opener').on("click", function(){
      var search_bar = $('.top-search-bar');
      if(search_bar.hasClass('open')){
        search_bar.removeClass('open');
      }else{
        search_bar.addClass('open');
      }
      return false;
    });
    /* ----- Search open close Start  ------ */
  }

  function owlcarousel_slider () {
    /* ------------ OWL Slider Start  ------------- */

      /* ---- Testimonial and Main-Banner Start ---- */
      $("#client, .main-banner").owlCarousel({
     
        //navigation : true,  Show next and prev buttons
        slideSpeed : 300,
        paginationSpeed : 400,
        autoPlay: false,
        pagination:true,
        singleItem:true,
        navigation:true
      });
      /* ----- Testimonial and Main-Banner End  ------ */
      return false;
    /* ------------ OWL Slider End  ------------- */
  }

  function scrolltop_arrow () {
   /* ---- Page Scrollup JS Start ---- */
   //When distance from top = 250px fade button in/out
    var scrollup = $('#scrollup');
    var headertag = $('header');
    var mainfix = $('.main');
    $(window).scroll(function(){
      if ($(this).scrollTop() > 250) {
          scrollup.fadeIn(300);
      } else {
          scrollup.fadeOut(300);
      }

      /* header-fixed JS Start */
      if ($(this).scrollTop() > 70){
         headertag.addClass("header-fixed");
      }
      else{ 
         headertag.removeClass("header-fixed");
      }

      /* main-fixed JS Start */
      if ($(this).scrollTop() >70){
         mainfix.addClass("main-fixed");
      }
      else{ 
         mainfix.removeClass("main-fixed");
      }
      /* ---- Page Scrollup JS End ---- */
    });
    
    //On click scroll to top of page t = 1000ms
    scrollup.on("click", function(){
        $("html, body").animate({ scrollTop: 0 }, 1000);
        return false;
    });
  }

  function custom_tab() {
    /* ------------ Account Tab JS Start ------------ */
    $('.account-tab-stap').on('click', 'li', function() {
        $('.account-tab-stap li').removeClass('active');
        $(this).addClass('active');
        
        $(".account-content").fadeOut();
        var currentLiID = $(this).attr('id');
        $("#data-"+currentLiID).fadeIn();
        return false;
    });
    /* ------------ Account Tab JS End ------------ */
  }

  /* Price-range Js Start */
  function price_range () {
      $( "#slider-range" ).slider({
      range: true,
      min: 0,
      max: 800,
      values: [ 75, 500 ],
      slide: function( event, ui ) {
      $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
      }
      });
      $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
      " - $" + $( "#slider-range" ).slider( "values", 1 ) );
  }
  /* Price-range Js End */

  /* Product Detail Page Tab JS Start */
  function description_tab () {
    $("#tabs li a").on("click", function(e){
      var title = $(e.currentTarget).attr("title");
      $("#tabs li a , .tab_content li div").removeClass("selected")
      $(".tab-"+title +", .items-"+title).addClass("selected")
      $("#items").attr("class","tab-"+title);

      return false;
    });
  }

  $('li.search-box').on('click', function(){
    $('.sidebar-search-wrap').addClass('open').siblings().removeClass('open');
    return false;
  });

  /*Search-box-close-button*/
  function search_close() {
    $('.search-closer').on('click', function() {
        var sidebar = $('.sidebar-navigation');
        var nav_icon = $('.navbar-toggle i');
        if(sidebar.hasClass('open')){
          //sidebar.removeClass('open');
        }else{
          sidebar.addClass('open');
          nav_icon.addClass('fa-search-close');
          nav_icon.removeClass('fa-search-bars');
        }

        $('.sidebar-search-wrap').removeClass('open');
        return false;
    });
  }


  /* Product Detail Page Tab JS End */
  $(document).ready(function() {
    owlcarousel_slider(); price_range (); responsive_dropdown(); description_tab (); custom_tab (); scrolltop_arrow (); search_open (); search_close();
  });

  $( window ).on( "resize", function() {
  
  });
});

  $( window ).on( "load", function() {
    // Animate loader off screen
    $(".se-pre-con").fadeOut("slow");
  });
