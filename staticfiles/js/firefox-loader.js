/**
 * Firefox-specific CSS loader
 * Detects Firefox browser and loads firefox-fixes.css
 * Has zero impact on Chrome and other browsers
 */

(function() {
    'use strict';
    
    /**
     * Detect if browser is Firefox
     * @returns {boolean} true if Firefox, false otherwise
     */
    function isFirefox() {
        // Check multiple Firefox identifiers for reliability
        return typeof InstallTrigger !== 'undefined' || 
               navigator.userAgent.toLowerCase().indexOf('firefox') > -1 ||
               navigator.userAgent.toLowerCase().indexOf('fxios') > -1;
    }
    
    /**
     * Load Firefox-specific CSS file
     */
    function loadFirefoxCSS() {
        // Create link element
        var link = document.createElement('link');
        link.rel = 'stylesheet';
        link.type = 'text/css';
        link.href = '/static/css/firefox-fixes.css';
        link.id = 'firefox-fixes-css';
        
        // Add to document head
        document.head.appendChild(link);
        
        // Optional: Add data attribute to body for debugging
        document.body.setAttribute('data-browser', 'firefox');
        
        // Log for development (can be removed in production)
        if (window.console) {
            console.log('Firefox detected - loaded firefox-fixes.css');
        }
    }
    
    /**
     * Get screen resolution info for debugging
     */
    function logScreenInfo() {
        if (window.console && isFirefox()) {
            var screenInfo = {
                width: window.screen.width,
                height: window.screen.height,
                availWidth: window.screen.availWidth,
                availHeight: window.screen.availHeight,
                pixelRatio: window.devicePixelRatio || 1,
                colorDepth: window.screen.colorDepth
            };
            
            console.log('Firefox Screen Info:', screenInfo);
            
            // Check if 4K resolution
            if (screenInfo.width >= 3840 && screenInfo.height >= 2160) {
                console.log('4K (3840x2160) display detected');
                document.body.setAttribute('data-resolution', '4k');
            }
        }
    }
    
    /**
     * Apply Firefox-specific positioning fix for stacked-cards
     * This runs after the stackedCards.js library initializes
     * Moves container down 7cm from center
     */
    function applyFirefoxPositioning() {
        if (!isFirefox()) return;
        
        // Wait for stackedCards to initialize
        setTimeout(function() {
            var stackedCardsContainer = document.querySelector('.stacked-cards');
            if (stackedCardsContainer) {
                // Force positioning to persist - moved down 7cm from center
                stackedCardsContainer.style.setProperty('justify-content', 'center', 'important');
                stackedCardsContainer.style.setProperty('align-items', 'center', 'important');
                stackedCardsContainer.style.setProperty('min-height', '100vh', 'important');
                stackedCardsContainer.style.setProperty('padding-top', '7cm', 'important');
                stackedCardsContainer.style.setProperty('box-sizing', 'border-box', 'important');
                
                if (window.console) {
                    console.log('Firefox: Applied stacked-cards positioning (7cm down)');
                }
            }
                // Force phase button font size at 915px landscape in Firefox
                if (window.matchMedia('(max-width: 915px) and (orientation: landscape)').matches) {
                    var phaseButtons = document.querySelectorAll('#phase-selection-container .btn-group .btn');
                        var overrideFontSize = function() {
                            phaseButtons.forEach(function(btn, idx) {
                                if (idx < 4) {
                                    btn.style.setProperty('font-size', '2.5px', 'important');
                                    btn.style.fontSize = '2.5px';
                                    btn.style.setProperty('color', 'red', 'important');
                                } else if (idx === 4) {
                                    btn.style.setProperty('font-size', '8px', 'important');
                                    btn.style.fontSize = '8px';
                                    btn.style.setProperty('color', 'red', 'important');
                                }
                            });
                        };
                        // Apply immediately and then every 500ms for 5 seconds
                        overrideFontSize();
                        var intervalId = setInterval(overrideFontSize, 500);
                        setTimeout(function() {
                            clearInterval(intervalId);
                        }, 5000);
                        if (window.console) {
                            console.log('Firefox: Forced phase button font size for 915px landscape (interval applied)');
                        }
                }
        }, 500); // Wait 500ms for stackedCards.js to finish
    }
    
    /**
     * Initialize on DOM ready
     */
    function init() {
        // Only proceed if Firefox
        if (isFirefox()) {
            loadFirefoxCSS();
            logScreenInfo();
            
            // Apply positioning fix after everything loads
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', applyFirefoxPositioning);
            } else {
                applyFirefoxPositioning();
            }
            
            // Also reapply on window load (double-check)
            window.addEventListener('load', applyFirefoxPositioning);
            
        } else if (window.console) {
            console.log('Non-Firefox browser detected - Chrome styles will be used');
        }
    }
    
    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        // DOM already loaded
        init();
    }
    
})();
