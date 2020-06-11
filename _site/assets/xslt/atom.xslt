<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:atom="http://www.w3.org/2005/Atom">
<xsl:output method="html" encoding="utf-8" />
<xsl:template match="/atom:feed">
	<xsl:text disable-output-escaping="yes">&lt;!DOCTYPE html &gt;</xsl:text>
	<html>
	<head>
		<xsl:text disable-output-escaping="yes"><![CDATA[
		<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Atom Feed (Styled)</title>

    <link rel="stylesheet" type="text/css" href="https://staging.ego-n.org/assets/css/styles_feeling_responsive.css">

  

	<script src="https://staging.ego-n.org/assets/js/modernizr.min.js"></script>

	<script src="https://ajax.googleapis.com/ajax/libs/webfont/1.5.18/webfont.js"></script>
	<script>
		WebFont.load({
			google: {
				families: [ 'Lato:400,700,400italic:latin', 'Volkhov::latin' ]
			}
		});
	</script>

	<noscript>
		<link href='http://fonts.googleapis.com/css?family=Lato:400,700,400italic%7CVolkhov' rel='stylesheet' type='text/css'>
	</noscript>


	<!-- Search Engine Optimization -->
	<meta name="description" content="Open, inter-grid-level and cross-sectoral planning instrument for the optimal use and expansion of the electrical grid and flexibility options in Germany">
	
	
	
	
	
	
	<link rel="canonical" href="https://staging.ego-n.org/assets/xslt/atom.xslt">


	<!-- Facebook Open Graph -->
	<meta property="og:title" content="Atom Feed (Styled)">
	<meta property="og:description" content="Open, inter-grid-level and cross-sectoral planning instrument for the optimal use and expansion of the electrical grid and flexibility options in Germany">
	<meta property="og:url" content="https://staging.ego-n.org/assets/xslt/atom.xslt">
	<meta property="og:locale" content="en_EN">
	<meta property="og:type" content="website">
	<meta property="og:site_name" content="eGo<sup>n</sup>">
	
	


	

	<link type="text/plain" rel="author" href="https://staging.ego-n.org/humans.txt">

	

	

	

	

	

	

	

	

	

	

	

	

	

	


	

		]]></xsl:text>
	</head>
	<body id="top-of-page">
		<xsl:text disable-output-escaping="yes"><![CDATA[
		
<div id="navigation" class="sticky">
  <nav class="top-bar" role="navigation" data-topbar>
    <ul class="title-area">
      <li class="name">
        <h1 class="">
          <a href="https://staging.ego-n.org"><img class="top-bar__logo" src="https://staging.ego-n.org/assets/img/logo_egon_top_nav.svg"></a>
        </h1>
      </li>
       <!-- Remove the class "menu-icon" to get rid of menu icon. Take out "Menu" to just have icon alone -->
      <li class="toggle-topbar menu-icon"><a href="#"><span></span></a></li>
    </ul>
    <section class="top-bar-section">

      <ul class="left">
        

              

          
          

            
            
              
              <li><a  href="https://staging.ego-n.org/tools_data/">Tools &amp; Data</a></li>
              <li class="divider"></li>
              

            
            
          
        

              

          
          

            
            
              
              <li><a  href="https://staging.ego-n.org/publications/">Publications</a></li>
              <li class="divider"></li>
              

            
            
          
        

              

          
          

            
            
              
              <li><a  href="https://staging.ego-n.org/partners/">Partners</a></li>
              <li class="divider"></li>
              

            
            
          
        
        
      </ul>
    </section>
  </nav>
</div><!-- /#navigation -->

		

<div id="masthead-no-image-header">
	<div class="row">
		<div class="small-12 columns">
			<a id="logo" href="https://staging.ego-n.org/" title="eGo<sup>n</sup> – energy Grid optimization of n flexibilities">
				<img src="https://staging.ego-n.org/assets/img/logo_egon_top_nav.svg" alt="eGo<sup>n</sup> – energy Grid optimization of n flexibilities">
			</a>
		</div><!-- /.small-12.columns -->
	</div><!-- /.row -->
</div><!-- /#masthead -->








		


<div class="alert-box warning text-center"><p>This <a href="https://en.wikipedia.org/wiki/RSS" target="_blank">Atom feed</a> is meant to be used by <a href="https://en.wikipedia.org/wiki/Template:Aggregators" target="_blank">RSS reader applications and websites</a>.</p>
</div>



		]]></xsl:text>
		<header class="t30 row">
	<p class="subheadline"><xsl:value-of select="atom:subtitle" disable-output-escaping="yes" /></p>
	<h1>
		<xsl:element name="a">
			<xsl:attribute name="href">
				<xsl:value-of select="atom:id" />
			</xsl:attribute>
			<xsl:value-of select="atom:title" />
		</xsl:element>
	</h1>
</header>
<ul class="accordion row" data-accordion="">
	<xsl:for-each select="atom:entry">
		<li class="accordion-navigation">
			<xsl:variable name="slug-id">
				<xsl:call-template name="slugify">
					<xsl:with-param name="text" select="atom:id" />
				</xsl:call-template>
			</xsl:variable>
			<xsl:element name="a">
				<xsl:attribute name="href"><xsl:value-of select="concat('#', $slug-id)"/></xsl:attribute>
				<xsl:value-of select="atom:title"/>
				<br/>
				<small><xsl:value-of select="atom:updated"/></small>
			</xsl:element>
			<xsl:element name="div">
				<xsl:attribute name="id"><xsl:value-of select="$slug-id"/></xsl:attribute>
				<xsl:attribute name="class">content</xsl:attribute>
				<h1>
					<xsl:element name="a">
						<xsl:attribute name="href"><xsl:value-of select="atom:id"/></xsl:attribute>
						<xsl:value-of select="atom:title"/>
					</xsl:element>
				</h1>
				<xsl:value-of select="atom:content" disable-output-escaping="yes" />
			</xsl:element>
		</li>
	</xsl:for-each>
</ul>

		<xsl:text disable-output-escaping="yes"><![CDATA[
		    <div id="up-to-top" class="row">
      <div class="small-12 columns" style="text-align: right;">
        <a class="iconfont" href="#top-of-page">&#xf108;</a>
      </div><!-- /.small-12.columns -->
    </div><!-- /.row -->


    <footer id="footer-content" class="bg-grau">


      <div id="subfooter">
        <div class="row">
          <div class="columns medium-3 subfooter__logo">
            <img src="https://staging.ego-n.org/images/eGon_logo_noborder_transbg.svg" alt="egon logo">
          </div>
          <div class="columns medium-9 subfooter__links">
            <div id="subfooter-right" class="credits credits--imprint">
              
                <a href="/imprint/" target="_blank" class="" title="Imprint">Imprint</a>
              
            </div>
            <!-- <section id="subfooter__copyright"  class="small-6 columns credits"> -->
            <div id="subfooter-left"  class="credits">
              <div class="subfooter-left__icons"> <img src="https://staging.ego-n.org/images/cc.svg" alt="CC" style="height:24px;"> <img src="https://staging.ego-n.org/images/by.svg" alt="BY" style="height:24px;"></div><p class="subfooter-left__text">Content of this webpage - except for the partner logos - is licensed under <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" class="">CC-BY-4.0</a> conditions</p>
            </div>
            <div id="subfooter-left" class="credits">
              <p>Created with <a href="http://jekyllrb.com/" target="_blank">Jekyll</a> based on <a href="http://phlow.github.io/feeling-responsive/">Feeling Responsive</a>.</p>
            </div>
          </div>
        </div>
      </div><!-- /#subfooter -->
    </footer>

		


<script src="https://staging.ego-n.org/assets/js/javascript.min.js"></script>














		]]></xsl:text>
	</body>
	</html>
</xsl:template>
<xsl:template name="slugify">
	<xsl:param name="text" select="''" />
	<xsl:variable name="dodgyChars" select="' ,.#_-!?*:;=+|&amp;/\\'" />
	<xsl:variable name="replacementChar" select="'-----------------'" />
	<xsl:variable name="lowercase" select="'abcdefghijklmnopqrstuvwxyz'" />
	<xsl:variable name="uppercase" select="'ABCDEFGHIJKLMNOPQRSTUVWXYZ'" />
	<xsl:variable name="lowercased"><xsl:value-of select="translate( $text, $uppercase, $lowercase )" /></xsl:variable>
	<xsl:variable name="escaped"><xsl:value-of select="translate( $lowercased, $dodgyChars, $replacementChar )" /></xsl:variable>
	<xsl:value-of select="$escaped" />
</xsl:template>
</xsl:stylesheet>
