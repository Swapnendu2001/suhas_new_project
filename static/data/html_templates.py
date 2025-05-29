BLOGS_TEMPLATE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>News Page Dev</title>
    <link rel="icon" type="image/png" href="static/icon/website_icon.png" />
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/@phosphor-icons/web@2.0.3"></script>
    
    <link
    href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap"
    rel="stylesheet"
    />
    <link
    href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@600&family=Inter:wght@500&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,700&display=swap"
    rel="stylesheet"
    />
    
    <script>
    /* Define custom fonts in Tailwind (optional, better in tailwind.config.js) */
    tailwind.config = {
        theme: {
        extend: {
            fontFamily: {
            jakarta: ['"Plus Jakarta Sans"', "sans-serif"],
            "helvetica-now": ['"Helvetica Now Display"', "sans-serif"],
            helvetica: ['"Helvetica"', "sans-serif"],
            "ibm-plex": ['"IBM Plex Sans"', "sans-serif"],
            inter: ['"Inter"', "sans-serif"],
            },
            backgroundImage: {
            "header-banner":
                "url('digital-marketing-agency-website-banner-ad-template-lzytv.png')",
            "hero-gradient":
                "linear-gradient(0deg, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('https://picsum.photos/1920/1080')", // Placeholder image used for gradient bg
            "podcast-bg":
                "linear-gradient(360deg, rgba(255, 255, 255, 0) 74.02%, #FFFFFF 100%), linear-gradient(180deg, rgba(255, 255, 255, 0) 61.61%, #FFFFFF 100%), url('Your paragraph text (8).png')",
            "cta-bg":
                "linear-gradient(0deg, rgba(0, 0, 0, 0.69), rgba(0, 0, 0, 0.69)), url('Screenshot 2024-09-18 at 9.57.41\u202FPM.png')",
            "gradient-line":
                "linear-gradient(90deg, #000000 0%, #9747FF 100%)",
            },
        },
        },
    };
    </script>
    <script>
    document.addEventListener("DOMContentLoaded", function () {
        const mobileMenuButton = document.getElementById("mobile-menu-button");
        const mobileMenu = document.getElementById("mobile-menu");

        mobileMenuButton.addEventListener("click", function () {
        mobileMenu.classList.toggle("hidden");
        mobileMenuButton.classList.toggle("hamburger-active");

        if (!mobileMenu.classList.contains("hidden")) {
            mobileMenu.classList.add("slide-down");
        } else {
            mobileMenu.classList.remove("slide-down");
        }
        });
    });
    </script>
    <style>
    @media screen and (max-width: 768px) {
        .hero-text {
        font-size: 28px !important; 
        line-height: 36px !important;
        }

        .article-container {
        padding-left: 20px !important;
        padding-right: 20px !important;
        }

        .toc-container {
        padding: 10px !important;
        }
    }

    @import url("https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@600&family=Inter:wght@500&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,700&display=swap");
    @font-face {
        font-family: "Helvetica Now Display";
        src: local("Helvetica Neue"), local("Helvetica"), local("Arial"),
        sans-serif; /* Basic fallback */
        font-weight: 700;
    }
    @font-face {
        font-family: "Helvetica";
        src: local("Helvetica Neue"), local("Helvetica"), local("Arial"),
        sans-serif; /* Basic fallback */
        font-weight: 400;
    }
    ::-webkit-scrollbar {
        display: none;
    }

    body {
        -ms-overflow-style: none;
        scrollbar-width: none;
    }
    @keyframes slideDown {
        from {
        transform: translateY(-10px);
        opacity: 0;
        }
        to {
        transform: translateY(0);
        opacity: 1;
        }
    }

    .slide-down {
        animation: slideDown 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    :root {
        --clr-dark-black: #121212;
        --clr-bdr-gray: #2a2a2a;
        --clr-white: #fff;
        --clr-primary: #9747ff;
        --clr-primary-light: #cda7ff;
        --clr-gray-800: #1e1e1e;
    }

    .mobile-menu-item {
        padding: 0.875rem 1rem;
        background: var(--clr-dark-black);
        border-bottom: solid 1px var(--clr-bdr-gray);
        color: var(--clr-white);
        cursor: pointer;
        display: flex;
        align-items: center;
        transition: background-color 0.2s ease;
    }

    .mobile-menu-item:hover {
        background-color: #1a1a1a;
    }

    .mobile-menu-item:active {
        background-color: #252525;
    }

    .item-title {
        flex-grow: 1;
        margin-left: 0.75rem;
        font-weight: 500;
    }

    .hamburger-line {
        transition: all 0.3s ease;
    }

    .hamburger-active .hamburger-line:nth-child(1) {
        transform: translateY(7px) rotate(45deg);
    }

    .hamburger-active .hamburger-line:nth-child(2) {
        opacity: 0;
    }

    .hamburger-active .hamburger-line:nth-child(3) {
        transform: translateY(-7px) rotate(-45deg);
    }

    .search-input {
        transition: all 0.2s ease;
    }

    .search-input:focus {
        box-shadow: 0 0 0 2px rgba(151, 71, 255, 0.5);
    }

    @keyframes shine {
        from {
        transform: translateX(-100%);
        }
        to {
        transform: translateX(100%);
        }
    }

    .login-btn {
        transition: all 0.2s ease;
    }

    .login-btn:hover {
        transform: translateY(-1px);
        box-shadow: 0 2px 8px rgba(205, 167, 255, 0.4);
    }
    /* TOC container enhancements */
    aside .p-6 {
        scrollbar-width: thin;
        scrollbar-color: #3533cd #f5f5f5;
        scroll-behavior: smooth;
        transition: all 0.3s ease;
    }

    .toc-container {
        scrollbar-width: thin;
        scrollbar-color: #3533cd #f5f5f5;
        scroll-behavior: smooth;
        transition: all 0.3s ease;
    }

    /* Custom scrollbar for webkit browsers */
    aside .p-6::-webkit-scrollbar,
    .toc-container::-webkit-scrollbar {
        width: 6px;
    }

    aside .p-6::-webkit-scrollbar-track,
    .toc-container::-webkit-scrollbar-track {
        background: #f5f5f5;
        border-radius: 10px;
    }

    aside .p-6::-webkit-scrollbar-thumb,
    .toc-container::-webkit-scrollbar-thumb {
        background: rgba(53, 51, 205, 0.5);
        border-radius: 10px;
    }

    /* Smooth transitions for TOC links */
    .toc-link {
        transition: color 0.3s ease, font-weight 0.2s ease,
        border-color 0.3s ease;
    }

    /* Active indicator animation */
    .toc-link.text-\[\#3533CD\] {
        position: relative;
    }

    .toc-link.text-\[\#3533CD\]::after {
        content: "";
        position: absolute;
        right: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 4px;
        height: 70%;
        background-color: #3533cd;
        border-radius: 2px;
        animation: fadeIn 0.3s ease;
    }      @keyframes fadeIn {
        from {
        opacity: 0;
        }
        to {
        opacity: 1;
        }
    }      /* Mobile TOC arrow styling for better touch targets */
    @media screen and (max-width: 1023px) {
        .toc-arrow {
        padding: 8px;
        margin: -8px;
        cursor: pointer;
        border-radius: 4px;
        transition: background-color 0.2s ease;
        position: relative;
        z-index: 10;
        }
        
        .toc-arrow:hover {
        background-color: rgba(53, 51, 205, 0.1);
        }
    }
    </style>
</head>
<body class="font-poppins bg-white text-gray-800">
    <header class="w-full bg-black relative">
    
        <div class="hidden lg:flex flex-row justify-center items-center px-20 py-[10px] gap-[70px] h-[113px]">
            <img src="static/images/header_logo.png" alt="Brands Out Loud Logo" class="w-20 h-20 flex-shrink-0">
            <nav class="flex flex-col items-stretch w-[700px] h-[93px] py-[14px] px-[18px] gap-[10px]">
                <div class="flex flex-row justify-end items-center w-full gap-[60px] px-[30px]">
                    <a href="#" class="text-white font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Careers </a>
                    <a href="#" class="text-white font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Podcast </a>
                    <a href="#" class="text-white font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Register </a>
                    <a href="#" class="bg-[#CDA7FF] rounded-[2px] px-2.5 py-0.5 text-[#0D0D0D] font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Login </a>
                </div>
                <div class="w-full h-[1px] bg-gradient-to-r from-black to-[#9747FF]"></div>
                <div class="flex flex-row justify-end items-center w-full gap-[60px] px-2">
                    <a href="#" class="text-[#C4C3FF] font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Newsletters </a>
                    <a href="#" class="text-[#C4C3FF] font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Magazine </a>
                    
                    <a href="#" class="text-[#C4C3FF] font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Startups </a>
                    <a href="#" class="text-[#C4C3FF] font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Business </a>
                </div>
            </nav>
        </div>

    
    <div class="flex lg:hidden items-center h-[68px] w-full bg-[#0D0D0D]">

        <button id="mobile-menu-button" aria-label="Toggle Menu" class="h-full px-4 flex flex-col justify-center items-center space-y-[5px] bg-transparent focus:outline-none transition-colors duration-200 ease-in-out">
        <span class="hamburger-line block w-6 h-[2px] bg-white rounded-full"></span>
        <span class="hamburger-line block w-6 h-[2px] bg-white rounded-full"></span>
        <span class="hamburger-line block w-6 h-[2px] bg-white rounded-full"></span>
        </button>

        <div class="h-full flex items-center px-3 flex-shrink-0">
        <img src="static/icon/website_icon.png" alt="Brands Out Loud Logo" class="h-10 w-auto"/>
        </div>

        <div class="flex-grow px-3">
        <div class="relative">
            <input type="text" placeholder="Search..." class="search-input w-full bg-[#1e1e1e] text-white text-sm rounded-full pl-10 pr-4 py-2.5 border border-[#2a2a2a] focus:outline-none focus:border-[#9747FF] transition-all"/>
            <div class="absolute inset-y-0 left-0 flex items-center pl-3.5 pointer-events-none">
            <i class="ph ph-magnifying-glass text-gray-400 text-lg"></i>
            </div>
        </div>
        </div>
    </div>

    
    <div id="mobile-menu" class="hidden lg:hidden absolute top-[68px] left-0 w-full bg-[#121212] z-50 shadow-lg border-t border-[#2a2a2a] overflow-hidden">
        <div class="">
        <div class="px-4 py-3">
            <a href="#" class="login-btn block w-full text-center bg-gradient-to-r from-[#9747FF] to-[#CDA7FF] rounded-full px-4 py-2.5 text-white font-medium text-sm shadow-lg hover:-translate-y-0.5 transition-all duration-300 relative overflow-hidden">
            <span class="relative z-10 flex items-center justify-center gap-2">
                <i class="ph ph-sign-in text-lg"></i>
                <span>Login</span>
            </span>
            <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent -translate-x-full animate-[shine_2s_infinite]"></div>
            </a>
        </div>

        <div class="mobile-menu-item">
            <i class="ph ph-book-open text-white text-lg"></i>
            <span class="item-title">Magazine</span>
            <i class="ph ph-caret-right"></i>
        </div>

        <div class="mobile-menu-item">
            <i class="ph ph-lightning text-white text-lg"></i>
            <span class="item-title">Startups</span>
            <i class="ph ph-caret-right"></i>
        </div>

        <div class="mobile-menu-item">
            <i class="ph ph-envelope-open text-white text-lg"></i>
            <span class="item-title">Newsletters</span>
            <i class="ph ph-caret-right"></i>
        </div>

        <div class="mobile-menu-item">
            <i class="ph ph-newspaper text-white text-lg"></i>
            <span class="item-title">Podcast</span>
            <i class="ph ph-caret-right"></i>
        </div>

        <div class="mobile-menu-item">
            <i class="ph ph-buildings text-white text-lg"></i>
            <span class="item-title">Business</span>f
            <i class="ph ph-caret-right"></i>
        </div>

        <div class="mobile-menu-item">
            <i class="ph ph-briefcase text-white text-lg"></i>
            <span class="item-title">Careers</span>
            <i class="ph ph-caret-right"></i>
        </div>
        </div>
    </div>
    </header>
    
    <main class="w-full px-4 sm:px-8 md:px-[65px] py-[21px] relative article-container">
        <article class="mb-8 md:mb-12 relative">
            <div class="relative w-full h-[300px] md:h-[478px]">
                <div class="absolute inset-0 bg-hero-gradient bg-cover bg-center"></div>
                <img src="[[main_page_image]]" alt="[[main_page_image_alt]]" class="w-full h-full object-cover opacity-40 mix-blend-multiply"/>
            </div>

            <div class="relative bg-white md:w-full w-[420px] md:ml-[6.85rem] ml-[-1.5rem] max-w-[1175px] h-auto mx-auto -mt-[40px] sm:-mt-[60px] md:-mt-[76px] p-4 sm:p-6 md:p-8 z-10">
                <h1 class="font-jakarta font-medium text-[28px] sm:text-[34px] md:text-[42px] lg:text-[50px] leading-[1.2] md:leading-[1.25] capitalize text-black mb-3 md:mb-4 text-center hero-text">
                    [[main_page_title]]
                </h1>
                <div class="flex justify-center items-center gap-2 text-center mb-4">
                    <p class="font-jakarta font-semibold text-[11px] sm:text-[12px] md:text-[14px] leading-[100.9%] text-black"> [[author_name]] </p>
                    <span class="text-black">- -</span>
                    <p class="font-jakarta font-normal text-[11px] sm:text-[12px] md:text-[14px] leading-[100.9%] text-black"> [[publish_date]] </p>
                </div>
            </div>

            <p class="font-jakarta font-medium text-[18px] md:text-[22px] leading-[26px] md:leading-[30px] text-[#636363] text-center mt-6 md:mt-8 max-w-[1175px] mx-auto px-2 md:px-0">
            [[blog_summary]]
            </p>

            <hr class="border-t border-black my-8 md:my-12 w-full md:w-[90%] lg:w-[87rem] mx-auto"/>
        </article>
    
        <div class="block lg:hidden px-4 mt-8">
            <div class="relative toc-container p-5 bg-white rounded-xl border-gray-100">
                <h2 class="text-xl font-bold text-[#3533CD] mb-4 border-b pb-3">Table of Contents</h2>
                
                [[table_of_contents_mobile_menu]]
                
                <div class="mt-6 space-y-4 border-t pt-5">
                    <button class="w-full h-[45px] bg-[#3533CD] rounded-xl flex items-center justify-center text-white font-jakarta font-medium text-[16px] leading-[120%] hover:bg-opacity-90 transition-colors shadow-md">
                        <i class="ph ph-download mr-2"></i>Download Article as PDF
                    </button>
                    <div class="flex items-center flex-wrap">
                        <div class="relative inline-flex items-center justify-center gap-2 bg-[#3533CD] rounded-xl h-[45px] px-4 cursor-pointer hover:bg-opacity-90 transition-colors shadow-md">
                            <span class="text-white font-jakarta font-medium text-[16px] leading-[120%] text-center" style="width: 7rem">
                                <i class="ph ph-share-network mr-2"></i>Share
                            </span>
                        </div>
                        <div class="flex space-x-3 ml-3">
                            <img src="static/images/whatsapp_logo.png" alt="WhatsApp" class="w-[35px] h-[35px] object-contain hover:opacity-80 transition-opacity"/>
                            <img src="static/images/insta_logo.png" alt="Instagram" class="w-[35px] h-[35px] object-contain hover:opacity-80 transition-opacity"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-[360px_1fr] gap-8 md:gap-12 mt-4 md:mt-8" style="margin-right: 0; margin-left: 0; padding: 0 0.5rem">
            <aside class="sticky top-8 h-8rem lg:order-1 self-start md:mt-[0rem] mt-[-57rem]">
                <div class="p-6 flex flex-col w-full rounded-xl bg-white border-gray-100 hidden lg:block overflow-y- max-h-[calc(100vh-4rem)]" style="scroll-behavior: smooth">
                    <h2 class="text-2xl font-bold text-[#3533CD] mb-6 border-b pb-3">Table of Contents</h2>
                    
                    [[table_of_contents_desktop_menu]]

                    <div class="mt-6 space-y-4 border-t pt-5">
                        <button class="w-full h-[45px] bg-[#3533CD] rounded-xl flex items-center justify-center text-white font-jakarta font-medium text-[16px] leading-[120%] hover:bg-opacity-90 transition-colors shadow-md">
                            <i class="ph ph-download mr-2"></i>Download Article as PDF
                        </button>
                        <div class="flex items-center flex-wrap">
                            <div class="relative inline-flex items-center justify-center gap-2 bg-[#3533CD] rounded-xl h-[45px] px-4 cursor-pointer hover:bg-opacity-90 transition-colors shadow-md">
                                <span class="text-white font-jakarta font-medium text-[16px] leading-[120%] text-center" style="width: 7rem">
                                    <i class="ph ph-share-network mr-2"></i>Share
                                </span>
                            </div>
                            <div class="flex space-x-3 ml-3">
                                <img src="static/images/whatsapp_logo.png" alt="WhatsApp" class="w-[35px] h-[35px] object-contain hover:opacity-80 transition-opacity"/>
                                <img src="static/images/insta_logo.png" alt="Instagram" class="w-[35px] h-[35px] object-contain hover:opacity-80 transition-opacity"/>
                            </div>
                        </div>
                    </div>
                </div>
            </aside>

            <section class="space-y-6 md:space-y-5 text-justify order-1 lg:order-2" >
            
            [[actual_blog_content]]
            
            </section>
        </div>

        <section class="w-full max-w-7xl mx-auto px-4 md:px-8 py-9 my-8">
            <div class="flex flex-col md:flex-row items-stretch gap-8">
                <div class="h-auto py-6 md:py-0 md:h-[32rem] w-full md:w-1/2 md:shrink-0 bg-gradient-to-r from-[#3533CD] to-[#0A0A24] rounded-[15px] p-4 md:p-8 flex flex-col items-center justify-center text-center text-white">
                    <h2 class="font-helvetica-now font-bold text-2xl md:text-4xl leading-tight mb-3 md:mb-4"> Leadership Spotlight </h2>
                        <div class="flex flex-col items-center gap-3 md:gap-4">
                            <div class="w-[100px] h-[100px] sm:w-[120px] sm:h-[120px] md:w-[160px] md:h-[160px] bg-[url('[[leadership_spotlight_image]]')] bg-cover bg-center rounded-full shrink-0"></div>
                            <div class="flex flex-col items-center">
                                <h3 class="font-jakarta font-normal text-lg sm:text-xl md:text-2xl leading-tight mb-1" > [[leader_name]] </h3>
                                <p class="font-jakarta font-normal text-base md:text-lg leading-tight mb-2 md:mb-3"> [[leader_designation]] </p>
                                <p class="font-jakarta font-normal text-sm md:text-base leading-relaxed mb-3 md:mb-4 max-w-xs md:max-w-sm" >
                                    [[leader_brief_description]]
                                </p>
                                <a href="[[link_to_leadership_webstories]]" class="inline-block hover:opacity-90 transition-opacity" >
                                    <img src="static/images/webstories_button.png" alt="Web Stories" class="w-[110px] h-[31px] md:w-[140px] md:h-[40px]" />
                                </a>
                            </div>
                        </div>
                </div>
                <a class="w-full md:w-1/2 h-80 md:h-auto bg-cover bg-center rounded-[15px] mt-4 md:mt-0 bg-[url([[ad_banner_beside_leaderhip_spotlight]])]"></a>
            </div>
        </section>

        <a href="[[link_to_ad_banner_below_leadership_spotlight]]" class="block w-full h-[120px] sm:h-[160px] md:h-[236px] my-8 md:my-12">
            <img src="[[ad_banner_under_leadership_section]]" alt="Advertisement" class="w-full h-full object-cover" />
        </a>

        [[more_in_business_posts]]

    </main>
    <section class="w-full aspect-[120/47] relative bg-contain bg-no-repeat bg-center bg-[url(static/images/9_out_of_10.png)]" style="margin-bottom: -1%">
        <a href="#" class="absolute bottom-[15%] left-[9%] w-[15%] max-w-[250px] hover:opacity-90 transition-opacity">
            <img src="static/images/checkot_button.png" alt="Checkout Podcast Button" class="block w-full h-auto"/>
        </a>
    </section>
    <section class="w-full aspect-[120/47] relative bg-contain bg-no-repeat bg-center bg-[url(static/images/fuel_ambition.png)]" style="margin-bottom: -1%">
        <a href="#" class="absolute bottom-[18%] left-[50%] -translate-x-1/2 w-[20%] max-w-[300px] hover:opacity-90 transition-opacity">
            <img src="static/images/checkout_magazine_button.png" alt="Checkout Magazine Button" class="block w-full h-auto"/>
        </a>
    </section>
    <footer class="w-full bg-black px-4 sm:px-6 md:px-[111px] pt-[40px] md:pt-[70px] pb-[20px] md:pb-[30px] relative text-white">
        <div class="flex flex-row flex-wrap justify-around items-start gap-6 md:gap-16 mb-8 md:mb-[100px] pt-6 md:pt-0 text-center sm:text-left">
            <div class="w-auto flex flex-col items-center sm:items-start order-1 mb-6 sm:mb-0 flex-shrink-0">
                <div class="w-[80px] h-[80px] sm:w-[100px] sm:h-[100px] md:w-[161px] md:h-[161px] bg-contain bg-no-repeat bg-center sm:bg-left bg-[url(static/images/header_logo.png)] mb-2 flex-shrink-0" loading="lazy"></div>
            </div>
            <div class="w-auto order-2 flex-shrink-0">
                <div class="font-helvetica font-bold text-sm md:text-base leading-[90%] text-[#8B8B8B] mb-3 md:mb-[19px] uppercase">Quick Links</div>
                <ul class="list-none p-0 m-0 space-y-2 md:space-y-[17px]">
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">Home</a></li>
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">About Us</a></li>
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">Careers</a></li>
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">Web Stories</a></li>
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">Magazine</a></li>
                </ul>
            </div>
            <div class="w-auto order-3 flex-shrink-0">
                <div class="font-helvetica font-bold text-sm md:text-base leading-[90%] text-[#8B8B8B] mb-3 md:mb-[20px] uppercase">News</div>
                <ul class="list-none p-0 m-0 space-y-2 md:space-y-[17px]">
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">Business</a></li>
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">Startup</a></li>
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">AI</a></li>
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">Entrepreneur</a></li>
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">Events</a></li>
                </ul>
            </div>
        </div>
        <div class="border-t border-white/30 w-full my-[30px] md:my-[40px]"></div>
        <div class="flex flex-col md:flex-row justify-between items-center">
            <div class="block mb-6 md:mb-4 w-full md:w-auto text-center md:text-left">
                <div class="font-helvetica font-bold text-sm md:text-base leading-[90%] text-[#8B8B8B] mb-[12px] md:mb-[15px] uppercase">Social Links</div>
                <div class="flex justify-center md:justify-start space-x-4">
                    <a href="#" aria-label="Instagram" class="text-white hover:text-[#C4C3FF] transition-colors duration-200">
                        <svg class="w-5 h-5 md:w-6 md:h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"></svg>
                            <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/>
                        </svg>
                    </a>
                    <a href="#" aria-label="Facebook" class="text-white hover:text-[#C4C3FF] transition-colors duration-200">
                        <svg class="w-5 h-5 md:w-6 md:h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                            <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                        </svg>
                    </a>
                    <a href="#" aria-label="X (Twitter)" class="text-white hover:text-[#C4C3FF] transition-colors duration-200">
                        <svg class="w-5 h-5 md:w-6 md:h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"></svg>
                            <path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/>
                        </svg>
                    </a>
                    <a href="#" aria-label="YouTube" class="text-white hover:text-[#C4C3FF] transition-colors duration-200">
                        <svg class="w-5 h-5 md:w-6 md:h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"></svg>
                            <path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
                        </svg>
                    </a>
                    <a href="#" aria-label="LinkedIn" class="text-white hover:text-[#C4C3FF] transition-colors duration-200">
                        <svg class="w-5 h-5 md:w-6 md:h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"></svg>
                            <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                        </svg>
                    </a>
                </div>
            </div>
            <div class="flex flex-col md:flex-row justify-between items-center gap-4 md:gap-[20px] flex-wrap mb-6 md:mb-[40px]">
                <a href="#" class="font-jakarta font-bold text-sm md:text-base leading-[20px] text-white no-underline hover:text-[#C4C3FF] uppercase">Advertise With Us</a>
            </div>
            <div class="text-center md:text-left col-span-1 lg:col-span-1 flex flex-col items-center md:items-start">
                <div class="font-helvetica font-bold text-base leading-[90%] text-[#8B8B8B] mb-[20px] uppercase">Subscribe to Newsletter</div>
                <form class="flex flex-row items-stretch gap-2 w-full max-w-md sm:hidden">
                    <input type="email" placeholder="Enter your email" required class="flex-grow h-[40px] bg-white border-none rounded-[4px] px-[15px] text-black placeholder:text-gray-500 focus:ring-2 focus:ring-bol-purple" style="left: 1rem; position: relative"/>
                    <input type="image" src="static/images/subscribe_button.png" alt="Subscribe" class="h-[40px] w-auto cursor-pointer hover:opacity-90 transition duration-150 ease-in-out shrink-0" style="left: -1rem; position: relative"/>
                </form>
                <form class="hidden sm:flex sm:flex-row items-stretch gap-2 w-full max-w-md">
                    <input type="email" placeholder="Enter your email" required class="flex-grow h-[40px] bg-white border-none rounded-[4px] px-[15px] text-black placeholder:text-gray-500 focus:ring-2 focus:ring-bol-purple"/>
                    <input type="image" src="static/images/subscribe_button.png" alt="Subscribe" class="h-[40px] w-auto cursor-pointer hover:opacity-90 transition duration-150 ease-in-out shrink-0" style="left: -2rem; position: relative"/>
                </form>
            </div>
        </div>
        <div class="block">
            <div class="border-t border-white/30 w-full my-[30px] md:my-[40px]"></div>
            <div class="w-full text-center font-helvetica font-bold text-xs md:text-base leading-[90%] text-white/70 mt-[20px]">© 2025 BRANDSOUTLOUD All Rights Reserved</div>
        </div>
    </footer>
    <script>
      const stripSection = document.querySelector(".strip-section");
      if (stripSection) {
        const stripContent = stripSection.querySelector(".animate-marquee");
        if (stripContent && stripContent.children.length > 0) {
          const contentWidth = stripContent.scrollWidth / 2;
          const containerWidth = stripSection.offsetWidth;
          stripContent.innerHTML += stripContent.innerHTML;
        }
      }
      // Enhanced TOC with auto-scrolling functionality
      document.addEventListener("DOMContentLoaded", function () {
        const tocDesktop = document.querySelector("aside .p-6");
        const tocMobile = document.querySelector(".toc-container");
        const tocLinks = document.querySelectorAll(".toc-link");
        const sections = document.querySelectorAll("h2[id], h3[id], p[id]");
        // Colors and styles for active/inactive states
        const activeColorClass = "text-[blue]";
        const inactiveColorClass = "text-gray-800";
        const activeFontWeightClass = "font-bold";
        const inactiveFontWeightClass = "font-medium";
        const activeBorderClass = "border-[#3533CD]";
        const inactiveBorderClass = "border-gray-200";        // Collapsible TOC functionality - different behavior for mobile and desktop
        const tocToggleLinks = document.querySelectorAll(
          "a[data-toggle-target]"
        );
        tocToggleLinks.forEach((link) => {
          const arrowIcon = link.querySelector(".toc-arrow");
          const textDiv = link.querySelector("div");
          // Handle arrow clicks for mobile
          if (arrowIcon) {
            arrowIcon.addEventListener("click", function (event) {
              event.preventDefault();
              event.stopPropagation();
              const targetId = link.getAttribute("data-toggle-target");
              const targetElement = document.querySelector(targetId);
              if (targetElement) {
                targetElement.classList.toggle("hidden");
                arrowIcon.classList.toggle("rotate-180");
              }
            });
          }
          // Handle text clicks for navigation
          if (textDiv) {
            textDiv.addEventListener("click", function (event) {
              const href = link.getAttribute("href");
              if (href && href.startsWith("#")) {
                event.preventDefault();
                const targetElement = document.querySelector(href);
                if (targetElement) {
                  targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
              }
            });
          }
          // For desktop, maintain original behavior
          link.addEventListener("click", function (event) {
            const isMobile = window.innerWidth < 1024;
            if (!isMobile) {
              const targetId = this.getAttribute("data-toggle-target");
              const targetElement = document.querySelector(targetId);
              if (targetElement) {
                targetElement.classList.toggle("hidden");
                if (arrowIcon) {
                  arrowIcon.classList.toggle("rotate-180");
                }
              }
            }
          });
        });
        // Handle sub-category links (those without data-toggle-target)
        const subCategoryLinks = document.querySelectorAll('.toc-link:not([data-toggle-target])');
        subCategoryLinks.forEach((link) => {
          link.addEventListener("click", function (event) {
            const href = this.getAttribute("href");
            if (href && href.startsWith("#")) {
              event.preventDefault();
              const targetElement = document.querySelector(href);
              if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
              }
            }
          });
        });
        // Enhanced scrollspy with TOC auto-scrolling
        function activateTocLink() {
          let currentSectionId = "";
          let currentParentSectionId = "";
          const scrollPosition = window.scrollY;
          const offset = 150; // Adjust based on header height
          let activeLink = null;
          // Find current section in view
          sections.forEach((section) => {
            const sectionTop = section.offsetTop;
            if (scrollPosition >= sectionTop - offset) {
              currentSectionId = section.getAttribute("id");
              // Determine parent H2 section
              let parentH2 = null;
              if (section.tagName === "H2") {
                parentH2 = section;
              } else {
                // Find preceding H2
                let previousElement = section.previousElementSibling;
                while (previousElement) {
                  if (
                    previousElement.tagName === "H2" &&
                    previousElement.hasAttribute("id")
                  ) {
                    parentH2 = previousElement;
                    break;
                  }
                  previousElement = previousElement.previousElementSibling;
                }
                if (!parentH2) {
                  const parentDiv = section.closest("div");
                  if (parentDiv) {
                    const h2InDiv = parentDiv.querySelector("h2[id]");
                    if (h2InDiv) parentH2 = h2InDiv;
                  }
                }
              }
              if (parentH2) {
                currentParentSectionId = parentH2.getAttribute("id");
              } else if (section.tagName === "H2") {
                currentParentSectionId = currentSectionId;
              }
            }
          });
          // Update TOC link styles and expand sections
          tocLinks.forEach((link) => {
            const linkHref = link.getAttribute("href");
            const linkTargetId = linkHref ? linkHref.substring(1) : null;
            const isH2Link = link.classList.contains("toc-h2-link");
            const parentTocSection = link.closest(".toc-section");
            const parentSectionDataId = parentTocSection
              ? parentTocSection.dataset.sectionId
              : null;
            // Reset styles
            link.classList.remove(activeFontWeightClass);
            link.classList.add(inactiveFontWeightClass);
            link.classList.replace(activeColorClass, inactiveColorClass);
            // Border classes for subcategory links
            if (!isH2Link) {
              link.classList.replace(activeBorderClass, inactiveBorderClass);
            }
            // Highlight active link
            if (linkTargetId === currentSectionId) {
              link.classList.add(activeFontWeightClass);
              link.classList.remove(inactiveFontWeightClass);
              link.classList.replace(inactiveColorClass, activeColorClass);
              if (!isH2Link) {
                link.classList.replace(inactiveBorderClass, activeBorderClass);
              }
              activeLink = link; // Store active link for scrolling
            }
            // Highlight parent H2 if child is active
            else if (
              isH2Link &&
              parentSectionDataId === currentParentSectionId
            ) {
              link.classList.add(activeFontWeightClass);
              link.classList.remove(inactiveFontWeightClass);
            }
          });          // Auto-expand/collapse TOC sections - disabled for mobile
          document.querySelectorAll(".toc-section").forEach((tocSection) => {
            const sectionId = tocSection.dataset.sectionId;
            const subcategoriesDiv =
              tocSection.querySelector(".toc-subcategories");
            const arrowIcon = tocSection.querySelector(".toc-arrow");
            const isMobile = window.innerWidth < 1024;
            if (subcategoriesDiv && arrowIcon && !isMobile) {
              // Only auto-expand/collapse for desktop
              if (sectionId === currentParentSectionId) {
                // Expand current section
                subcategoriesDiv.classList.remove("hidden");
                arrowIcon.classList.add("rotate-180");
              } else {
                // Collapse other sections
                subcategoriesDiv.classList.add("hidden");
                arrowIcon.classList.remove("rotate-180");
              }
            }
          });
          // Scroll active link into view (for both mobile and desktop TOC)
          if (activeLink) {
            // Handle desktop TOC scrolling
            if (tocDesktop && window.innerWidth >= 1024) {
              const linkTop = activeLink.offsetTop;
              const tocTop = tocDesktop.scrollTop;
              const tocHeight = tocDesktop.clientHeight;
              // Check if link is not visible in the current view
              if (linkTop < tocTop || linkTop > tocTop + tocHeight - 50) {
                // Smoothly scroll to the active link
                tocDesktop.scrollTo({
                  top: linkTop - tocHeight / 3,
                  behavior: "smooth",
                });
              }
            }
            // Handle mobile TOC scrolling
            if (tocMobile && window.innerWidth < 1024) {
              const linkTop = activeLink.offsetTop;
              const tocTop = tocMobile.scrollTop;
              const tocHeight = tocMobile.clientHeight;
              if (linkTop < tocTop || linkTop > tocTop + tocHeight - 40) {
                tocMobile.scrollTo({
                  top: linkTop - tocHeight / 3,
                  behavior: "smooth",
                });
              }
            }
          }
        }
        // Initialize active state on load
        activateTocLink();
        // Update on scroll
        window.addEventListener("scroll", activateTocLink);
      });
    </script>
  </body>
</html>  
    """

more_in_business_single_post_template = r"""<div class="bg-white p-3 flex gap-4 h-auto min-h-[120px] md:h-[151px] transition-shadow hover:shadow-md">
            <img src="[[post_image]]" alt="[[post_alt]]" class="w-[90px] md:w-[127px] h-auto md:h-[121px] object-cover flex-none"/>
            <div class="flex flex-col">
                <span class="font-jakarta font-bold text-[10px] md:text-[12px] leading-[24px] md:leading-[30px] text-black uppercase">BUSINESS</span>
                <a href="#" class="font-jakarta font-medium text-[14px] md:text-[16px] leading-[22px] md:leading-[25px] underline text-black grow hover:text-[#3533CD]">
                    [[post_title]]</a>
                <span
                    class="font-jakarta italic font-bold text-[10px] md:text-[12px] text-black mt-auto"
                    >[[post_author]] -- [[poat_date]]</span
                >
            </div>
          </div>"""