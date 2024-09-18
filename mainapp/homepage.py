from random import choice
data = {
    'headline' : "unlock profitable crypto",
    'headline2' : " & gambling offers",
    'sub_headline' : "Welcome to RyptocurrencyStakes, where innovation meets opportunity. Explore special cryptocurrency investments and top-tier gambling deals. Dive into the world of cryptocurrency and gambling with our expert-backed offers.",
    'what_we_offer' : "Discover Unmatched Offers Tailored to Your Needs",
    'what_we_offer2' : "Discover Tailored Offers",

    # Hero Section
    'hero_cta_primary' : "Get Started Today",
    'hero_cta_secondary' : "Learn More",

    'what_we_offer_list' : [
        # Exclusive Cryptocurrency Opportunities
        {
            'title' : "Exclusive Cryptocurrency Opportunities",
            'description' : "Explore exclusive handpicked cryptocurrency investment platforms curated by industry experts to maximize your profit potential with precision and reliability.",
            'cta' : "Learn More"
        },

    # Top-Tier Sports Betting and Casino Deals
        {
            'title' : "Top-Tier Sports Betting and Casino Deals",
            'description' : "Experience the thrill of top-tier sports betting and casino gaming with the best odds and bonuses from trusted partners.",
            'cta' : "Start Betting"    
        },

    # Real-Time Market Insights and Data
       {
            'title' : "Real-Time Market Insights and Data",
            'description' : "Stay ahead with real-time data and market insights tailored to your needs. Make informed decisions in both crypto trading and betting.",
            'cta' : "Get Insights"   
        },

    # User-Friendly Platform with 24/7 Support
        {
            'title' : "User-Friendly Platform with 24/7 Support",
            'description' : "Navigate with confidence, whether you're betting or investing, with our intuitive platform and 24/7 dedicated support.",
            'cta' : "Join Now"    
        },
    ],
    # Featured Offers
    'featured_offers_title' : "Our Top Picks for You",
    'crypto_offers' : [
        {
            'title' : "QUANTUM GENIUS GPT",
            'excerpt' : "Unlock trading potential with just $250",
            'description' : "Want to Outsmart the Market? Unleash the power of Quantum Genius GPT, an innovative trading platform that leverages advanced AI and quantum computing to optimize your trading strategies.",
            'features' : ["High-accuracy AI-Driven Insights", "Tailored trade preferences for personalized strategies", "24/7 Expert Support to guide your journey", "Transparent with No Hidden Fees", "Fast Withdrawals processed within 24 hours", "Robust Risk Management for secure trading"],
            'cta' : "Discover QUANTUM GENIUS GPT",
            'image' : 'assets/images/quantum_genius.png',
            'url' : "https://llrxqw.abadat5rckc.com/c/70f85c3757d382de",
            'tab' : "1"
        },
        {
        'title' : "BITCOIN 360 AI",
        'excerpt' : "Minimum Investment Starting at $250",
        'description' : "Take Your Crypto Trading to the Next Level with Bitcoin 360 AI - The Future of Automated Trading Is Here. Sign Up Now and Start Trading!",
        'features' : ["AI-Powered Trading Algorithms for maximized profits", "User-Friendly Interface", "24/7 Automated Trading", "Personalized Expert Guidance to optimize your strategy", "Fast and Secure Deposit & Withdrawals", "No Hidden Fees, Trade with Confidence"],
        'cta' : "Discover BITCOIN 360 AI",
        'image' : 'assets/images/bitcoin_360.png',
        'url' : "https://llrxqw.abadat5rckc.com/c/ddd7c0f04904feee",
        'tab' : "1"
    },
    {
        'title' : "FINANCE PHANTOM",
        'excerpt' : "Start with just $250",
        'description' : "Trade Smarter, Not Harder - Boost Your Trading Success with Finance Phantom's AI Advantage",
        'features' : ["AI-Driven Market Analysis for Optimal Trading Results", "24/7 Automated Trading - Never Miss a Market Move", "Friendly & Experienced Support Team Ready to Assist", "Secure and Safe Trading Environment", "Quick Withdrawals Processed within 24 Hours", "No Hidden Fees"],
        'cta' : "Discover FINANCE PHANTOM",
        'image' : 'assets/images/finance_phantom.png',
        'url' : "https://llrxqw.abadat5rckc.com/c/d83c1eef2e5f7450",
        'tab' : "1"
    }
    ],
    'gambling_offers' : [
                {
                    'title': 'FORTUNEJACK CASINO',
                    'excerpt': 'Get started and explore top-tier crypto casino games!',
                    'description': 'Discover the world of online crypto gambling at FortuneJack Casino, With over 1,500 games and seamless crypto transactions, FortuneJack provides a premier experience for both new and experienced players. ',
                    'features': [
                        'Over 1,500 Casino Games',
                        'Instant Crypto Deposits and Withdrawals',
                        'Live and Virtual Casino Options',
                        'Generous Bonuses and Promotions',
                        '24/7 Customer Support',
                        'Exclusive VIP Program for High Rollers'
                    ],
                    'cta': 'JOIN NOW!',
                    'image' : 'assets/images/fortunejack_casino.jpeg',
                    'url' : 'https://offerone.g2afse.com/click?pid=444&offer_id=48',
                    'tab' : '2'
                    
                },
                {
                 'title': 'CRYPTOLEO CASINO',
                 'excerpt': 'Elevate your gaming with crypto-powered bonuses and fast payouts.',
                 'description': 'CryptoLeo Casino offers an exhilarating gaming experience with the added benefit of seamless cryptocurrency transactions. From captivating slots to immersive live dealer games, players enjoy exclusive bonuses, lightning-fast crypto deposits, and withdrawals. Designed for both crypto experts and newcomers, CryptoLeo combines modern tech with exciting gameplay.',
                 'features': [
                        'Unlock exclusive crypto bonuses with every play',
                        'Play a diverse range of slots, table games, and live dealers',
                        'Instant, hassle-free crypto deposits and payouts',
                        'Mobile-first design for gaming anywhere, anytime',
                        'Unmatched security with advanced crypto encryption technology'
                      ],
                 'cta': 'PLAY NOW AT CRYPTOLEO CASINO',
                 'image' : 'assets/images/fortunejack_casino.jpeg',
                 'url' : 'https://offerone.g2afse.com/click?pid=444&offer_id=48',
                 'tab' : '2' 
                }, 
            {
                  'title': 'JOYA CASINO',
                  'excerpt': 'Experience unparalleled gaming and massive rewards at Joya Casino.',
                  'description': "Joya Casino brings you a world of excitement with a wide range of slot games, table games, and live dealers. With irresistible bonuses and promotions, the platform guarantees top-level security and lightning-fast payouts. Whether you're playing on mobile or desktop, Joya Casino delivers a smooth, thrilling experience designed for every level of player.",
                  'features': [
                    'Huge selection of thrilling slot games and live dealers',
                    'Massive bonuses for new and returning players',
                    'Super-fast payouts with no hidden fees',
                    'Mobile-optimized for gaming on the go',
                    'Top-notch security with encryption to safeguard your data'
                  ],
                  'cta': 'START WINNING AT JOYA CASINO',
                  'image' : 'assets/images/fortunejack_casino.jpeg',
                  'url' : "https://taal.gotrackier.com/click?campaign_id=541&pub_id=710",
                  'tab' : "2" 
            },
            {
                  'title': 'NINEWIN CASINO',
                  'excerpt': 'Experience top-tier casino gaming with exciting features and rewards.',
                  'description': 'Ninewin Casino offers a vast array of casino games, from slots to table games and live dealers. It provides attractive bonuses for new users and has a seamless interface for a smooth experience. Users benefit from fast and secure payouts, ensuring a hassle-free withdrawal process. The platform guarantees top-level security with encryption and promotes responsible gaming.',
                  'features': [
                    'Huge variety of slot games and table games',
                    'Live dealer games for an immersive experience',
                    'Fast and secure payout system',
                    'Attractive bonuses for new and loyal players',
                    'Mobile-optimized for gaming on the go',
                    'High-level security with data encryption'
                  ],
                  'cta': 'SIGN UP NOW AT NINEWIN CASINO',
                  'image' : 'assets/images/fortunejack_casino.jpeg',
                  'url' : "https://taal.gotrackier.com/click?campaign_id=542&pub_id=710",
                  'tab' : "2" 
            }                   

    ],

    

    # Call to Action
    'cta_section_title' : "Elevate Your Game: Invest in Crypto, Bet with Confidence",
    'cta_primary_button' : "Sign Up Now",
    'cta_secondary_button' : "Explore Our Offers",

    # Who we are
    'who_we_are' : {
    'experience': "Over 6 Years of Expertise",
    'team': "With over six years of experience in online gambling and cryptocurrency, our team of experts in digital marketing, financial trading, and customer service is dedicated to bringing you top-tier offers and cutting-edge insights",
    'dedication': "Committed to Bringing You Top-Tier Offers and Insights"
    },
    # Partners
    'partners' : [
        {
            'partner_img' : "assets/images/quantum_genius.png",
            'partner_url' : "https://llrxqw.abadat5rckc.com/c/70f85c3757d382de"
         }, 
        {
            'partner_img' : "assets/images/bitcoin_360.png",
            'partner_url' : "https://llrxqw.abadat5rckc.com/c/ddd7c0f04904feee"
        }, 
        {
            'partner_img' : "assets/images/finance_phantom.png",
            'partner_url' : "https://llrxqw.abadat5rckc.com/c/d83c1eef2e5f7450"
        }
        ],
    
    # Mission
    
    'mission_taglines' : {
    'empower': "Empower You to Win Big",
    'invest': "Make Informed Investments",
    'entertain': "Enjoy Thrilling Entertainment",
    },
    'mission' : "At RyptocurrencyStakes, Our mission is to bring you the finest opportunities in betting, casinos, and cryptocurrency investments.",

    # Footer - About Us
    'footer_about_title' : "About Us",
    'footer_about_cta' : "Learn More About Us",

    # Footer - Quick Links
    'footer_links' : {
    'home': "Home",
    
    'about': "About Us",
    'about': "What We Offer",
    'contact': "Join Us",
    # 'privacy_policy': "Privacy Policy",
    # 'terms_of_service': "Terms of Service",
    # 'cookie_policy': "Cookie Policy",
    # 'affiliate_disclosure': "Affiliate Disclosure",
    # 'sitemap': "Sitemap",
    # 'support': "Support"
    'contact': "Contact Us",
    'about': "About Us",
    'crypto': "Crypto Offers",
    # 'gambling_offers': "Gambling Offers",
    'finance-phantom': "Finance Phantom",
    'bitcoin-360-ai': "Bitcoin 360 AI",
    'quantum-genius-gpt': "Quantum Genius GPT",
    # 'sitemap': "Sitemap",
    # 'support': "Support"
    },
    

    # Footer - Contact Information
    'footer_contact_email' : "contactus@rcs.com",

    # Footer - Social Media Links
    'footer_social_links' : {
        'facebook': "Facebook",
        'twitter': "Twitter",
        'linkedin': "LinkedIn"
    },
    'address' : "2B Bramble Street Coventry United Kingdom, CV1 2HT",
    'phone_no' : "+447553220982",

    # Disclaimer
    'disclaimer' : "Cryptocurrency trading and gambling involve significant risk. Prices can fluctuate widely, and you should only invest what you can afford to lose. Please consult with a financial advisor if you are unsure about the risks involved."
}

crypto_images = ["assets/images/crypto_trading.avif", "assets/images/crypto_trading2.avif", "assets/images/crypto_trading3.jpeg"]
gambling_images = ["assets/images/phonecasino.jpg", "assets/images/onlinecasino2.jpg", "assets/images/onlinecasino.jpg","assets/images/poker_bg.jpg","assets/images/poker_bg2.jpg","assets/images/laptopcasino.jpg"]

def generate_offers(offers_list):
    offers = []
    
    for offer in offers_list:
        # Create a slug by converting the title to lowercase and replacing spaces with hyphens
        offer_title = offer["title"].lower()
        slug = "-".join(offer_title.split())

        # Append the offer to the new list, including the slug
        
        offers.append({
            "slug": slug,
            "title": offer["title"],
            "image": choice(gambling_images),
            "logo" : offer["image"],
            "cta": offer["cta"],
            "url": offer["url"],
            "description": offer["description"],
            "excerpt": offer["excerpt"],
            "features": offer["features"],
            "tab": offer["tab"]
        })
        
    return offers

crypto_offers = generate_offers(data["crypto_offers"])
gambling_offers = generate_offers(data["gambling_offers"])
