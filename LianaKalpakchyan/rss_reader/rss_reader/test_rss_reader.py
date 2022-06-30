import unittest
from rss_reader import Reader

reader = Reader()
xml_content = """
<rss xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:media="http://search.yahoo.com/mrss/" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:nyt="http://www.nytimes.com/namespaces/rss/2.0" version="2.0">
<channel>
<title>NYT > Top Stories</title>
<link>https://www.nytimes.com</link>
<atom:link href="https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml" rel="self" type="application/rss+xml"/>
<description/>
<language>en-us</language>
<copyright>Copyright 2022 The New York Times Company</copyright>
<lastBuildDate>Thu, 30 Jun 2022 08:06:15 +0000</lastBuildDate>
<pubDate>Thu, 30 Jun 2022 06:34:56 +0000</pubDate>
<image>
<title>NYT > Top Stories</title>
<url>https://static01.nyt.com/images/misc/NYT_logo_rss_250x40.png</url>
<link>https://www.nytimes.com</link>
</image>
<item>
<title>In States Banning Abortion, a Growing Rift Over Enforcement</title>
<link>https://www.nytimes.com/2022/06/29/us/abortion-enforcement-prosecutors.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/us/abortion-enforcement-prosecutors.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/us/abortion-enforcement-prosecutors.html" rel="standout"/>
<description>A reluctance by some liberal district attorneys to bring criminal charges against abortion providers is already complicating the legal landscape in some states.</description>
<dc:creator>J. David Goodman and Jack Healy</dc:creator>
<pubDate>Wed, 29 Jun 2022 21:41:55 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Abortion</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Law and Legislation</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">District Attorneys</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">Texas</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/29/us/29abortion-enforcement03/29abortion-enforcement03-moth.jpg" width="151"/>
<media:credit>Callaghan O'Hare/Reuters</media:credit>
<media:description>Abortion rights protesters outside a courthouse in Houston. Some Democratic prosecutors are uneasy about declaring their districts safe havens for abortions, worried doing so could be used as grounds for their own removal by Republican leaders.</media:description>
</item>
<item>
<title>First Amendment Confrontation May Loom in Post-Roe Fight</title>
<link>https://www.nytimes.com/2022/06/29/business/media/first-amendment-roe-abortion-rights.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/business/media/first-amendment-roe-abortion-rights.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/business/media/first-amendment-roe-abortion-rights.html" rel="standout"/>
<description>Without a federal right to abortion, questions about how states can regulate speech about it suddenly become much murkier.</description>
<dc:creator>Jeremy W. Peters</dc:creator>
<pubDate>Wed, 29 Jun 2022 20:40:40 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Women and Girls</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Law and Legislation</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Dobbs v Jackson Women's Health Organization (Supreme Court Decision)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Freedom of Speech and Expression</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Abortion</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/29/business/29abortion-speech/merlin_209181351_b4d9c88b-5603-4bf8-9448-e98c53a30c46-moth.jpg" width="151"/>
<media:credit>Shuran Huang for The New York Times</media:credit>
<media:description>A demonstrator outside the Supreme Court on Sunday.</media:description>
</item>
<item>
<title>For Many Women, Roe Was About More Than Abortion. It Was About Freedom.</title>
<link>https://www.nytimes.com/2022/06/29/us/women-abortion-roe-wade.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/us/women-abortion-roe-wade.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/us/women-abortion-roe-wade.html" rel="standout"/>
<description>After the reversal of Roe v. Wade, some women are reconsidering their plans, including where they live, and wondering how best to channel their anger.</description>
<dc:creator>Julie Bosman</dc:creator>
<pubDate>Wed, 29 Jun 2022 07:00:13 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Abortion</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Dobbs v Jackson Women's Health Organization (Supreme Court Decision)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Roe v Wade (Supreme Court Decision)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Women and Girls</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Women's Rights</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">States (US)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Supreme Court (US)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Decisions and Verdicts</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">United States</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/28/us/28abortion-women-1-SWAP-2/28abortion-women-1-SWAP-2-moth.jpg" width="151"/>
<media:credit>Nina Robinson for The New York Times</media:credit>
<media:description>Yolanda Williams plans to live in rural Georgia with her daughter. She has considered whether they should live in a state where abortion could soon be severely restricted, but is unsure which corner of the country could be better.</media:description>
</item>
<item>
<title>How Zeldin’s Anti-Abortion Stance May Affect the N.Y. Governor’s Race</title>
<link>https://www.nytimes.com/2022/06/29/nyregion/abortion-lee-zeldin-governor.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/nyregion/abortion-lee-zeldin-governor.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/nyregion/abortion-lee-zeldin-governor.html" rel="standout"/>
<description>Representative Lee Zeldin, the Republican candidate for governor, said the decision to overturn Roe v. Wade was a victory for family, life and the Constitution.</description>
<dc:creator>Nicholas Fandos</dc:creator>
<pubDate>Wed, 29 Jun 2022 21:21:24 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Abortion</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Dobbs v Jackson Women's Health Organization (Supreme Court Decision)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Politics and Government</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Zeldin, Lee M</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Hochul, Kathleen C</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Elections, Governors</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">New York State</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/29/nyregion/29nygov-zeldin/29nygov-zeldin-moth.jpg" width="151"/>
<media:credit>Andrew Seng for The New York Times, Desiree Rios/The New York Times</media:credit>
<media:description>Gov. Kathy Hochul, right, is portraying her opponent, Lee Zeldin, as a Republican with right-wing views such as opposing abortion.</media:description>
</item>
<item>
<title>Jan. 6 Committee Subpoenas Pat Cipollone, Trump’s White House Counsel</title>
<link>https://www.nytimes.com/2022/06/29/us/politics/pat-cipollone-subpoena-jan-6.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/us/politics/pat-cipollone-subpoena-jan-6.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/us/politics/pat-cipollone-subpoena-jan-6.html" rel="standout"/>
<description>Mr. Cipollone, who repeatedly fought extreme plans to overturn the election, had resisted publicly testifying to the panel.</description>
<dc:creator>Luke Broadwater and Maggie Haberman</dc:creator>
<pubDate>Thu, 30 Jun 2022 02:56:58 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">United States Politics and Government</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Presidential Election of 2020</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Storming of the US Capitol (Jan, 2021)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">House Select Committee to Investigate the January 6th Attack</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Cipollone, Pat A</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Trump, Donald J</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/29/multimedia/29dc-cipollone-2/29dc-cipollone-1-moth.jpg" width="151"/>
<media:credit>Erin Schaff/The New York Times</media:credit>
<media:description>The House committee investigating the Jan. 6 attack said it needed to hear from Pat A. Cipollone “on the record, as other former White House counsels have done in other congressional investigations.”</media:description>
</item>
<item>
<title>Hutchinson Testimony Exposes Tensions Between Parallel Jan. 6 Inquiries</title>
<link>https://www.nytimes.com/2022/06/29/us/politics/jan-6-committee-justice-department-trump.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/us/politics/jan-6-committee-justice-department-trump.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/us/politics/jan-6-committee-justice-department-trump.html" rel="standout"/>
<description>That the House panel did not provide the Justice Department with transcripts of Cassidy Hutchinson’s interviews speaks to the panel’s reluctance to turn over evidence.</description>
<dc:creator>Glenn Thrush, Luke Broadwater and Michael S. Schmidt</dc:creator>
<pubDate>Thu, 30 Jun 2022 00:14:33 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Storming of the US Capitol (Jan, 2021)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">United States Politics and Government</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Democratic Party</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">House of Representatives</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">House Select Committee to Investigate the January 6th Attack</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Justice Department</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Republican Party</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/29/us/politics/29dc-justice-1/merlin_209280969_da03a812-750c-496f-97de-9e81fb71c7f8-moth.jpg" width="151"/>
<media:credit>Doug Mills/The New York Times</media:credit>
<media:description>Cassidy Hutchinson’s testimony sent shock waves through Washington, including the Justice Department, on Tuesday.</media:description>
</item>
<item>
<title>A More Muscular NATO Emerges as West Confronts Russia and China</title>
<link>https://www.nytimes.com/2022/06/29/world/europe/nato-expansion-ukraine-war.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/world/europe/nato-expansion-ukraine-war.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/world/europe/nato-expansion-ukraine-war.html" rel="standout"/>
<description>It is a fundamental shift for a military alliance born in the Cold War and scrambling to respond to a newly reshaped world.</description>
<dc:creator>Steven Erlanger and Michael D. Shear</dc:creator>
<pubDate>Thu, 30 Jun 2022 03:20:40 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">North Atlantic Treaty Organization</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">Russia</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">China</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Russian Invasion of Ukraine (2022)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Biden, Joseph R Jr</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Putin, Vladimir V</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Prisoners of War</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">United States International Relations</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">International Relations</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/29/world/29ukraine-nato-ledeall-1/29ukraine-nato-ledeall-1-moth.jpg" width="151"/>
<media:credit>Kenny Holston for The New York Times</media:credit>
<media:description>President Biden with the NATO secretary-general, Jens Stoltenberg, left, and Prime Minister Pedro Sánchez of Spain at the NATO summit in Madrid on Wednesday.</media:description>
</item>
<item>
<title>Patient and Confident, Putin Shifts Out of Wartime Crisis Mode</title>
<link>https://www.nytimes.com/2022/06/30/world/europe/putin-russia-nato-ukraine.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/30/world/europe/putin-russia-nato-ukraine.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/30/world/europe/putin-russia-nato-ukraine.html" rel="standout"/>
<description>Cloistered and spouting grievances at the start of the war on Ukraine, the Russian leader now appears publicly, projecting the aura of a calm, paternalistic leader shielding his people from the dangers of the world.</description>
<dc:creator>Anton Troianovski</dc:creator>
<pubDate>Thu, 30 Jun 2022 04:01:09 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Russian Invasion of Ukraine (2022)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Politics and Government</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">United States International Relations</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Embargoes and Sanctions</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">European Union</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">North Atlantic Treaty Organization</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Peter the Great (1672-1725)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Putin, Vladimir V</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">Caspian Sea</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">Russia</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">Ukraine</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/29/world/29russia-putin-01/29russia-putin-01-moth.jpg" width="151"/>
<media:credit>Getty Images</media:credit>
<media:description>President Vladimir Putin of Russia arriving in Ashgabat, the capital of Turkmenistan, on Wednesday to attend the Caspian Summit.</media:description>
</item>
<item>
<title>McKinsey Guided Companies at the Center of the Opioid Crisis</title>
<link>https://www.nytimes.com/2022/06/29/business/mckinsey-opioid-crisis-opana.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/business/mckinsey-opioid-crisis-opana.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/business/mckinsey-opioid-crisis-opana.html" rel="standout"/>
<description>The consulting firm offered clients “in-depth experience in narcotics,” from poppy fields to pills more powerful than Purdue’s OxyContin.</description>
<dc:creator>Chris Hamby and Michael Forsythe</dc:creator>
<pubDate>Wed, 29 Jun 2022 23:24:22 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Consultants</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Opioids and Opiates</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Pain-Relieving Drugs</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Drugs (Pharmaceuticals)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Drug Abuse and Traffic</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">OxyContin (Drug)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Poppies</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Acquired Immune Deficiency Syndrome</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Centers for Disease Control and Prevention</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Drug Enforcement Administration</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Food and Drug Administration</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Johnson & Johnson</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">McKinsey & Co</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Purdue Pharma</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">Appalachian Region</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">United States</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Endo</category>
<category domain="">Opana</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/28/multimedia/mckinsey-top/mckinsey-top-moth-v2.png" width="151"/>
<media:credit>Mark Weaver</media:credit>
</item>
<item>
<title>Truck Carrying Dead Migrants Passed Through U.S. Checkpoint</title>
<link>https://www.nytimes.com/2022/06/29/us/texas-migrants-deaths-truck.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/us/texas-migrants-deaths-truck.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/us/texas-migrants-deaths-truck.html" rel="standout"/>
<description>Border Patrol officials say truck traffic is too voluminous to check every vehicle at the dozens of immigration checkpoints on roadways near the border.</description>
<dc:creator>James Dobbins, J. David Goodman and Miriam Jordan</dc:creator>
<pubDate>Thu, 30 Jun 2022 03:24:56 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Illegal Immigration</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Immigration and Emigration</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Search and Seizure</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Trucks and Trucking</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Border Patrol (US)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Abbott, Gregory W (1957- )</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">Texas</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/29/us/29migrant-deaths-1/merlin_209243991_a32eccb6-ab46-4673-825c-b276dcf84515-moth.jpg" width="151"/>
<media:credit>Lisa Krantz for The New York Times</media:credit>
<media:description>Officials said that at least 53 people died from extreme heat inside a tractor-trailer that was abandoned in San Antonio, including migrants from Mexico, Honduras, Guatemala and El Salvador.</media:description>
</item>
<item>
<title>At Wimbledon, Maxime Cressy’s Throwback Style Helps Him Charge Forward</title>
<link>https://www.nytimes.com/2022/06/29/sports/tennis/wimbledon-cressy.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/sports/tennis/wimbledon-cressy.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/sports/tennis/wimbledon-cressy.html" rel="standout"/>
<description>We’re well past the glory days of the serve-and-volley style that took John McEnroe, Martina Navratilova and Pete Sampras to the Hall of Fame. Maxime Cressy is on a one-man revival mission.</description>
<dc:creator>Matthew Futterman</dc:creator>
<pubDate>Wed, 29 Jun 2022 20:50:23 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Wimbledon Tennis Tournament</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Cressy, Maxime</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/29/multimedia/29wimbledon-cressy/29wimbledon-cressy-moth.jpg" width="151"/>
<media:credit>Sebastien Bozon/Agence France-Presse — Getty Images</media:credit>
<media:description>For Maxime Cressy, playing at the net is a central part of his tennis strategy.</media:description>
</item>
<item>
<title>This Is What a Post-Roe Abortion Looks Like</title>
<link>https://www.nytimes.com/2022/06/29/opinion/abortion-pill-roe-wade.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/opinion/abortion-pill-roe-wade.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/opinion/abortion-pill-roe-wade.html" rel="standout"/>
<description>Self-managed abortion is not a substitute for having full reproductive rights. But it’s one of the best tools we have right now.</description>
<dc:creator>Ora DeKornfeld, Emily Holzknecht and Jonah M. Kessel</dc:creator>
<pubDate>Wed, 29 Jun 2022 09:00:12 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Abortion</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Law and Legislation</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">Texas</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Roe v Wade (Supreme Court Decision)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Mifeprex (RU-486)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">your-feed-opinionvideo</category>
</item>
<item>
<title>Women Will Save Us</title>
<link>https://www.nytimes.com/2022/06/29/opinion/women-midterm-elections.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/opinion/women-midterm-elections.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/opinion/women-midterm-elections.html" rel="standout"/>
<description>In the face of recent threats to the country, women have stepped up more than men.</description>
<dc:creator>Charles M. Blow</dc:creator>
<pubDate>Thu, 30 Jun 2022 00:55:06 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Project Democracy</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Democratic Party</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Women and Girls</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Storming of the US Capitol (Jan, 2021)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Dobbs v Jackson Women's Health Organization (Supreme Court Decision)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">United States Politics and Government</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Supreme Court (US)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Midterm Elections (2022)</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/29/opinion/29blow1/29blow1-moth.jpg" width="151"/>
<media:credit>Kendrick Brinson for The New York Times</media:credit>
</item>
<item>
<title>Cassidy Hutchinson Changes Everything</title>
<link>https://www.nytimes.com/2022/06/29/opinion/cassidy-hutchinson-january-6-committee.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/opinion/cassidy-hutchinson-january-6-committee.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/opinion/cassidy-hutchinson-january-6-committee.html" rel="standout"/>
<description>Her testimony delivered shocking and consequential revelations, but they have hardly been the only ones. </description>
<dc:creator>Norman Eisen</dc:creator>
<pubDate>Thu, 30 Jun 2022 00:32:34 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Storming of the US Capitol (Jan, 2021)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Fourteenth Amendment (US Constitution)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Watergate Affair</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">House of Representatives</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">House Select Committee to Investigate the January 6th Attack</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Secret Service</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Cipollone, Pat A</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Meadows, Mark R (1959- )</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Pence, Mike</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Trump, Donald J</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">United States</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">Georgia</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/30/opinion/29eisen2-BW/29eisen2-BW-moth.jpg" width="151"/>
<media:credit>Doug Mills/The New York Times</media:credit>
</item>
<item>
<title>The Supreme Court Takes Us Back … Way Back</title>
<link>https://www.nytimes.com/2022/06/29/opinion/roe-dobbs-abortion-supreme-court.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/opinion/roe-dobbs-abortion-supreme-court.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/opinion/roe-dobbs-abortion-supreme-court.html" rel="standout"/>
<description>Think about what the world was really like before Roe.</description>
<dc:creator>Gail Collins</dc:creator>
<pubDate>Thu, 30 Jun 2022 00:13:54 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Dobbs v Jackson Women's Health Organization (Supreme Court Decision)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Women and Girls</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Birth Control and Family Planning</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Abortion</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Pregnancy and Childbirth</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Supreme Court (US)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Stanton, Elizabeth Cady</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Thomas, Clarence</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Anthony, Susan B</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Vaughn, Hester</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Finkbine, Sherri</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/29/opinion/29collins-1/29collins-1-moth.jpg" width="151"/>
<media:credit>Mark Peterson/Redux for The New York Times</media:credit>
</item>
<item>
<title>‘This Really Changes Things’: Three Opinion Writers on Cassidy Hutchinson’s Jan. 6 Testimony</title>
<link>https://www.nytimes.com/2022/06/29/opinion/jan-6-hearings-cassidy-hutchinson.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/opinion/jan-6-hearings-cassidy-hutchinson.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/opinion/jan-6-hearings-cassidy-hutchinson.html" rel="standout"/>
<description>Bret Stephens and Michelle Cottle answer the question: Should Trump be indicted?</description>
<dc:creator>‘The Argument’</dc:creator>
<pubDate>Wed, 29 Jun 2022 19:16:40 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">audio-neutral-informative</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Storming of the US Capitol (Jan, 2021)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">United States Politics and Government</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">House Select Committee to Investigate the January 6th Attack</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Hutchinson, Cassidy</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Trump, Donald J</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Meadows, Mark R (1959- )</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Stephens, Bret (1973- )</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Cottle, Michelle</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Republican Party</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/29/opinion/29argument-image2/29argument-image2-moth.jpg" width="151"/>
<media:credit>Brandon Bell/Getty Images</media:credit>
</item>
<item>
<title>America’s Death Penalty Sentences Are Slowly Grinding to a Halt</title>
<link>https://www.nytimes.com/2022/06/29/opinion/death-penalty-executions.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/opinion/death-penalty-executions.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/opinion/death-penalty-executions.html" rel="standout"/>
<description>The numbers of executions and death sentences are falling.</description>
<dc:creator>Maurice Chammah</dc:creator>
<pubDate>Wed, 29 Jun 2022 09:00:23 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Capital Punishment</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Suits and Litigation (Civil)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">State Legislatures</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Polls and Public Opinion</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Sentences (Criminal)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Law and Legislation</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Minorities</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Civil Rights and Liberties</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">False Arrests, Convictions and Imprisonments</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">NAACP Legal Defense Fund</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Supreme Court (US)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">United States</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/27/opinion/00Chammah/00Chammah-moth.jpg" width="151"/>
<media:credit>George Rinhart/Corbis, via Getty Images</media:credit>
</item>
<item>
<title>Democrats Are Having a Purity-Test Problem at Exactly the Wrong Time</title>
<link>https://www.nytimes.com/2022/06/29/opinion/progressive-nonprofits-philanthropy.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/opinion/progressive-nonprofits-philanthropy.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/opinion/progressive-nonprofits-philanthropy.html" rel="standout"/>
<description>“It has become too easy for people to conflate disagreements about issues with matters of identity,” one nonprofit official says.</description>
<dc:creator>Thomas B. Edsall</dc:creator>
<pubDate>Thu, 30 Jun 2022 00:30:56 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Race and Ethnicity</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Black Lives Matter Movement</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">George Floyd Protests (2020)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Philanthropy</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Minorities</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Whites</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Appointments and Executive Changes</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Nonprofit Organizations</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Democratic Party</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/29/opinion/29edsall_1/29edsall_1-moth.jpg" width="151"/>
<media:credit>Paul LInse/Getty Images</media:credit>
</item>
<item>
<title>Is the Supreme Court Facing a Legitimacy Crisis?</title>
<link>https://www.nytimes.com/2022/06/29/opinion/supreme-court-legitimacy-crisis.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/opinion/supreme-court-legitimacy-crisis.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/opinion/supreme-court-legitimacy-crisis.html" rel="standout"/>
<description>Warnings of the court’s declining credibility are hardly new, but after Roe’s fall, they’ve intensified and moved well beyond the bench.</description>
<dc:creator>Spencer Bokat-Lindell</dc:creator>
<pubDate>Wed, 29 Jun 2022 22:00:04 +0000</pubDate>
<category domain="">debatable</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Abortion</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Roe v Wade (Supreme Court Decision)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Supreme Court (US)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Thomas, Clarence</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Bork, Robert H</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Same-Sex Marriage, Civil Unions and Domestic Partnerships</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Sotomayor, Sonia</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Alito, Samuel A Jr</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Kagan, Elena</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Breyer, Stephen G</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Rehnquist, William H</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/29/opinion/29debatable-image/29debatable-image-moth.jpg" width="151"/>
<media:credit>Illustration by The New York Times; photographs by Chip Somodevilla, Tasos Katopodis, and Samuel Corum, via Getty Images</media:credit>
</item>
<item>
<title>Modern Love Podcast: Left to Be Found</title>
<link>https://www.nytimes.com/2022/06/29/podcasts/modern-love-adoption-stories.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/podcasts/modern-love-adoption-stories.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/podcasts/modern-love-adoption-stories.html" rel="standout"/>
<description>Two women share their adoption stories — one a daughter, and the other a mother.</description>
<pubDate>Wed, 29 Jun 2022 20:00:08 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Women and Girls</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Adoptions</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">Hong Kong</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Love (Emotion)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Babies and Infants</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2020/10/15/us/00ModLove-Podcast-Promo-Art/00ModLove-Podcast-Promo-Art-moth.png" width="151"/>
<media:credit>Brian Rea</media:credit>
</item>
<item>
<title>7 Tips for House Plant Care</title>
<link>https://www.nytimes.com/2022/06/23/well/live/plant-care-tips.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/23/well/live/plant-care-tips.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/23/well/live/plant-care-tips.html" rel="standout"/>
<description>If you are known to turn a lush house plant into a rotting carcass, here are a few expert tips for making greenery thrive.</description>
<dc:creator>Melinda Wenner Moyer</dc:creator>
<pubDate>Mon, 27 Jun 2022 20:48:08 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Content Type: Service</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Weeds</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Gardens and Gardening</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Flowers and Plants</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Summer (Season)</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/24/well/24Well-NL-Plants/24Well-NL-Plants-moth.jpg" width="151"/>
<media:credit>Guillem Casasus</media:credit>
</item>
<item>
<title>Sensing the World Anew Through Other Species</title>
<link>https://www.nytimes.com/2022/06/24/books/review/podcast-ed-yong-immense-world-terry-alford-houses-of-their-dead.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/24/books/review/podcast-ed-yong-immense-world-terry-alford-houses-of-their-dead.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/24/books/review/podcast-ed-yong-immense-world-terry-alford-houses-of-their-dead.html" rel="standout"/>
<description>Ed Yong talks about “An Immense World,” and Terry Alford discusses “In the Houses of Their Dead.”</description>
<pubDate>Sat, 25 Jun 2022 01:14:36 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Books and Literature</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_ttl">An Immense World: How Animal Senses Reveal the Hidden Realms Around Us (Book)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Yong, Ed (1981- )</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Alford, Terry</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_ttl">In the Houses of Their Dead: The Lincolns, the Booths, and the Spirits (Book)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Animal Cognition</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Occult Sciences</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Lincoln, Abraham</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Booth, John Wilkes</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/23/books/review/24pod-cover/22BOOKYONG1-moth.png" width="151"/>
</item>
<item>
<title>Our Data Is a Curse, With or Without Roe</title>
<link>https://www.nytimes.com/2022/06/29/technology/abortion-data-privacy.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/technology/abortion-data-privacy.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/technology/abortion-data-privacy.html" rel="standout"/>
<description>There is so much digital information about us out there that we can’t possibly control it all.</description>
<dc:creator>Shira Ovide</dc:creator>
<pubDate>Wed, 29 Jun 2022 17:31:36 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">internal-sub-only-nl</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Data-Mining and Database Marketing</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Law and Legislation</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Abortion</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Privacy</category>
</item>
<item>
<title>Woman Is Fatally Shot While Pushing Baby in Stroller on Upper East Side</title>
<link>https://www.nytimes.com/2022/06/29/nyregion/upper-east-side-woman-shot-nyc.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/nyregion/upper-east-side-woman-shot-nyc.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/nyregion/upper-east-side-woman-shot-nyc.html" rel="standout"/>
<description>The shooting occurred near the intersection of Lexington Avenue and 95th Street, the police said. The 3-month-old child was unhurt.</description>
<dc:creator>Ed Shanahan</dc:creator>
<pubDate>Thu, 30 Jun 2022 05:22:31 +0000</pubDate>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/29/us/29strollershooting/29strollershooting-moth.jpg" width="151"/>
<media:credit>Dakota Santiago for The New York Times </media:credit>
<media:description>Investigators at the site of the fatal shooting of a 20-year-old woman on the Upper East Side. </media:description>
</item>
<item>
<title>Liz Cheney Calls Trump ‘a Domestic Threat That We Have Never Faced Before’</title>
<link>https://www.nytimes.com/2022/06/29/us/politics/liz-cheney-speech-trump.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/us/politics/liz-cheney-speech-trump.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/us/politics/liz-cheney-speech-trump.html" rel="standout"/>
<description>In a forceful speech, the congresswoman also denounced Republican leaders who had “made themselves willing hostages to this dangerous and irrational man.”</description>
<dc:creator>Maggie Haberman</dc:creator>
<pubDate>Thu, 30 Jun 2022 03:59:44 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Cheney, Liz</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Trump, Donald J</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">House Select Committee to Investigate the January 6th Attack</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">Wyoming</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Elections, House of Representatives</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Republican Party</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Conservatism (US Politics)</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/29/us/29midterm-briefing-cheney-speech-2/29midterm-briefing-cheney-speech-2-moth.jpg" width="151"/>
<media:credit>Kyle Grillot for The New York Times</media:credit>
<media:description>Representative Liz Cheney's address at the Ronald Reagan Presidential Library was met with a standing ovation. She is facing a tough Republican primary battle in Wyoming.</media:description>
</item>
<item>
<title>R. Kelly, R&B Star Who Long Evaded Justice, Is Sentenced to 30 Years</title>
<link>https://www.nytimes.com/2022/06/29/nyregion/r-kelly-racketeering-sex-abuse.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/nyregion/r-kelly-racketeering-sex-abuse.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/nyregion/r-kelly-racketeering-sex-abuse.html" rel="standout"/>
<description>The prison term marks the culmination of Mr. Kelly’s stunning downfall. In court, the women he victimized gave wrenching accounts. “I don’t know if I’ll ever be whole,” one said.</description>
<dc:creator>Troy Closson</dc:creator>
<pubDate>Wed, 29 Jun 2022 22:40:24 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Kelly, R</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Sex Crimes</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Child Abuse and Neglect</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Racketeering and Racketeers</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Human Trafficking</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/29/nyregion/29rkelly-leadall/merlin_195258624_2a6307f4-85ef-4bcd-9251-85906109a182-moth.jpg" width="151"/>
<media:credit>Matt Marton/Associated Press</media:credit>
<media:description>The sentencing in Brooklyn marks the culmination of a stunning downfall for R. Kelly, from a superstar hitmaker to a shunned artist whose legacy has become inextricable from his abuses.</media:description>
</item>
<item>
<title>A Young Black Man is Paralyzed and New Haven Officers are Investigated</title>
<link>https://www.nytimes.com/2022/06/29/nyregion/randy-cox-paralyzed-new-haven-police.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/nyregion/randy-cox-paralyzed-new-haven-police.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/nyregion/randy-cox-paralyzed-new-haven-police.html" rel="standout"/>
<description>Randy Cox, 36, was being transported in a police van when it came to a sudden stop on June 19. He is now in the hospital, barely able to move.</description>
<dc:creator>Ali Watkins</dc:creator>
<pubDate>Thu, 30 Jun 2022 02:23:47 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Police Brutality, Misconduct and Shootings</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Police Department (New Haven, Conn)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Gray, Freddie (1989-2015)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">New Haven (Conn)</category>
</item>
<item>
<title>Processed Meat and Health Risks: What to Know</title>
<link>https://www.nytimes.com/2022/06/29/well/eat/processed-meats.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/well/eat/processed-meats.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/well/eat/processed-meats.html" rel="standout"/>
<description>Here’s what the experts say.</description>
<dc:creator>Sophie Egan</dc:creator>
<pubDate>Wed, 29 Jun 2022 13:33:42 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Meat</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Cooking and Cookbooks</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Content Type: Service</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Hazardous and Toxic Substances</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Diet and Nutrition</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Colon and Colorectal Cancer</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Cancer</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Diabetes</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Alzheimer's Disease</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Salt</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Hot Dogs and Frankfurters</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Blood Pressure</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Oils and Fats</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/07/05/well/28ASKWELL-PROCESSED-MEAT1/merlin_208946991_127ebb11-a3d5-4303-bc21-84b18d410b40-moth.jpg" width="151"/>
<media:credit>Aileen Son for The New York Times</media:credit>
</item>
<item>
<title>The Foods That Keep You Hydrated</title>
<link>https://www.nytimes.com/2022/06/28/well/hydrating-foods.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/28/well/hydrating-foods.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/28/well/hydrating-foods.html" rel="standout"/>
<description>Water doesn’t have to come in eight 8-ounce glasses daily. Fresh fruits and vegetables, and various beverages, are viable sources of hydration.</description>
<dc:creator>Hannah Seo</dc:creator>
<pubDate>Tue, 28 Jun 2022 14:05:59 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Dehydration</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Heat and Heat Waves</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/07/05/well/27WELL-HYDRATING-FOODS3/27WELL-HYDRATING-FOODS3-moth.jpg" width="151"/>
<media:credit>Suzanne Saroff for The New York Times</media:credit>
</item>
<item>
<title>Do Prepackaged Salad Greens Lose Their Nutrients?</title>
<link>https://www.nytimes.com/2017/11/03/well/eat/do-prepackaged-salad-greens-lose-their-nutrients.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2017/11/03/well/eat/do-prepackaged-salad-greens-lose-their-nutrients.html</guid>
<atom:link href="https://www.nytimes.com/2017/11/03/well/eat/do-prepackaged-salad-greens-lose-their-nutrients.html" rel="standout"/>
<description>Some greens lose more nutrients than others with washing and storage.</description>
<dc:creator>Roni Caryn Rabin</dc:creator>
<pubDate>Tue, 13 Jul 2021 12:47:07 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Vitamins</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Salads</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Vitamin C</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Lettuce</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Spinach</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2017/11/07/science/ask-salad/ask-salad-moth.jpg" width="151"/>
<media:credit>Getty Images</media:credit>
</item>
<item>
<title>Can Technology Help Us Eat Better?</title>
<link>https://www.nytimes.com/2021/02/08/well/diet-glucose-monitor.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2021/02/08/well/diet-glucose-monitor.html</guid>
<atom:link href="https://www.nytimes.com/2021/02/08/well/diet-glucose-monitor.html" rel="standout"/>
<description>A new crop of digital health companies is using blood glucose monitors to transform the way we eat.</description>
<dc:creator>Anahad O’Connor</dc:creator>
<pubDate>Tue, 21 Dec 2021 14:04:39 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Diet and Nutrition</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Sugar</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Wearable Computing</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Diabetes</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Heart</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2021/02/09/science/05sci-well-bloodsugar-diet-REV/05sci-well-bloodsugar-diet-REV-moth-v2.jpg" width="151"/>
<media:credit>Leann Johnson</media:credit>
</item>
<item>
<title>Is Alkaline Water Really Better for You?</title>
<link>https://www.nytimes.com/2018/04/27/well/eat/alkaline-water-health-benefits.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2018/04/27/well/eat/alkaline-water-health-benefits.html</guid>
<atom:link href="https://www.nytimes.com/2018/04/27/well/eat/alkaline-water-health-benefits.html" rel="standout"/>
<description>What’s behind the claims that alkaline water will “energize” and “detoxify” the body and lead to “superior hydration”?</description>
<dc:creator>Alice Callahan</dc:creator>
<pubDate>Sat, 09 Jun 2018 00:27:38 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Water</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Diet and Nutrition</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Content Type: Service</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2018/05/01/well/01ask-water/ask-water-moth.jpg" width="151"/>
<media:credit>iStock</media:credit>
</item>
<item>
<title>Artists Scrutinize Nazi Family Past of Julia Stoschek</title>
<link>https://www.nytimes.com/2022/06/29/arts/julia-stoschek-nazi-family-past.html</link>
<guid isPermaLink="true">https://www.nytimes.com/2022/06/29/arts/julia-stoschek-nazi-family-past.html</guid>
<atom:link href="https://www.nytimes.com/2022/06/29/arts/julia-stoschek-nazi-family-past.html" rel="standout"/>
<description>As word circulated of a link between Julia Stoschek’s fortune and forced labor in World War II, some began questioning the ethics of working with the billionaire art patron.</description>
<dc:creator>Thomas Rogers</dc:creator>
<pubDate>Wed, 29 Jun 2022 18:42:33 +0000</pubDate>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Collectors and Collections</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Art</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">Holocaust and the Nazi Era</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">World War II (1939-45)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/des">High Net Worth Individuals</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Stoschek, Julia</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_org">Stoschek, Julia, Collection</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Brose, Max (1884-1968)</category>
<category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">Germany</category>
<media:content height="151" medium="image" url="https://static01.nyt.com/images/2022/06/28/arts/28berlin-collector14/28berlin-collector14-moth.jpg" width="151"/>
<media:credit>Gordon Welters for The New York Times</media:credit>
<media:description>Julia Stoschek said she embraced any inspection of her family fortune. “It’s very important that the art scene, as has been the case recently, looks at where money is coming from,” she said.</media:description>
</item>
</channel>
</rss>
"""
xml_link = 'https://news.yahoo.com/rss/'
xml_items = [{
                 'description': 'A reluctance by some liberal district attorneys to bring criminal charges against abortion providers is already complicating the legal landscape in some states.',
                 'image': 'https://static01.nyt.com/images/2022/06/29/us/29abortion-enforcement03/29abortion-enforcement03-moth.jpg',
                 'link': 'https://www.nytimes.com/2022/06/29/us/abortion-enforcement-prosecutors.html',
                 'pubDate': 'Wed, 29 Jun 2022 21:41:55 +0000',
                 'title': 'In States Banning Abortion, a Growing Rift Over Enforcement'}]
xml_title = 'NYT > Top Stories'
news_valid_link = 'https://news.yahoo.com/spit-disrespect-arrive-wimbledon-tennis-220151441.html'
news_invalid_link = 'https://www.cnbc/world-top-news/'


class RssTest(unittest.TestCase):
    def no_title_parse_xml_test(self):
        self.assertEqual(reader.parse_xml(''), ('Invalid source, provide a new one', []))

    def parse_xml_test(self):
        print(reader.parse_xml(xml_content,))
        self.assertEqual(reader.parse_xml(xml_content,),
                         ('BuzzFeed News', """[{'title': 'She Was One Year Away From Going To College. Then The Taliban Banned Her From School.', 'link': 'https://www.buzzfeednews.co
m/article/syedzabiullah/afghanistan-taliban-girls-school-ban', 'pubDate': 'Mon, 13 Jun 2022 20:32:05 -0400', 'image': 'No image found', 'description':
 '<h1>The policy prohibiting girls from attending school after sixth grade contradicts the regime’s previous promises to loosen restrictions on educat
ion rights.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-06/13/19/campaign_images/c453b771f93f/she-was-one-year-away-from-goi
ng-to-college-then--2-778-1655149050-7_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/syedzabiullah/afghanistan-taliban-girl
s-school-ban">View Entire Post &rsaquo;</a></p>'}, {'title': 'I, A Brit, Went To Tokyo, And Here Are 18 Things I Noticed That Are Pretty Effing Differ
ent From The UK', 'link': 'https://www.buzzfeed.com/sam_cleal/interesting-facts-japan-vs-uk', 'pubDate': 'Tue, 28 Jun 2022 00:52:02 -0400', 'image': '
No image found', 'description': '<h1>Yes, that is a rabbit on a lead.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-06/28/0/ca
mpaign_images/73cdc5cd6061/i-a-brit-went-to-tokyo-and-here-are-18-things-i-n-2-1163-1656377517-18_dblbig.jpg" /></p><hr /><p><a href="https://www.buzz
feed.com/sam_cleal/interesting-facts-japan-vs-uk">View Entire Post &rsaquo;</a></p>'}, {'title': 'Prince George, Princess Charlotte, And Prince Louis
Played A Starring Role In The Trooping The Colour', 'link': 'https://www.buzzfeednews.com/article/ellievhall/george-charlotte-louis-prince-princess-tr
ooping-colour', 'pubDate': 'Thu, 02 Jun 2022 21:25:05 -0400', 'image': 'No image found', 'description': '<h1>The Cambridge children rode in a carriage
 during the Queen\'s birthday parade as part of her Platinum Jubilee celebrations.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/20
22-06/2/18/campaign_images/4ccc9ca6031b/prince-george-princess-charlotte-and-prince-louis-2-537-1654193129-17_dblbig.jpg" /></p><hr /><p><a href="http
s://www.buzzfeednews.com/article/ellievhall/george-charlotte-louis-prince-princess-trooping-colour">View Entire Post &rsaquo;</a></p>'}, {'title': 'Ji
ll Biden Made A Surprise Visit To Ukraine To Meet With Their First Lady', 'link': 'https://www.buzzfeednews.com/article/davidmack/jill-biden-ukraine-f
irst-lady', 'pubDate': 'Mon, 09 May 2022 18:54:59 -0400', 'image': 'No image found', 'description': '<h1>Olena Zelenska had not been seen in public si
nce Russia\'s invasion of Ukraine began in February.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-05/9/18/campaign_images/020
c0602f06d/jill-biden-made-a-surprise-visit-to-ukraine-to-me-2-7123-1652122494-3_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/artic
le/davidmack/jill-biden-ukraine-first-lady">View Entire Post &rsaquo;</a></p>'}, {'title': 'The WHO Has Nearly Tripled Its Estimate Of The Pandemic’s
Death Toll', 'link': 'https://www.buzzfeednews.com/article/peteraldhous/who-covid-death-count-15-million', 'pubDate': 'Fri, 06 May 2022 11:25:05 -0400
', 'image': 'No image found', 'description': '<h1>The UN’s health agency has embraced statistical methods that put the true toll of the pandemic at ar
ound 15 million. Will it shock nations that are denying the severity of COVID-19 into action?</h1><p><img src="https://img.buzzfeed.com/buzzfeed-stati
c/static/2022-05/5/14/campaign_images/32b42d921348/the-who-has-nearly-tripled-its-estimate-of-the-pa-2-517-1651761061-0_dblbig.jpg" /></p><hr /><p><a
href="https://www.buzzfeednews.com/article/peteraldhous/who-covid-death-count-15-million">View Entire Post &rsaquo;</a></p>'}, {'title': 'A Former Mar
ine Was Freed From “Wrongful Detention” In Russia, But Concerns Remain For Brittney Griner And Others', 'link': 'https://www.buzzfeednews.com/article/
davidmack/brittney-griner-trevor-reed-paul-whelan-russia', 'pubDate': 'Thu, 28 Apr 2022 17:25:10 -0400', 'image': 'No image found', 'description': '<h
1>Trevor Reed\'s release from Russia highlighted concerns over the continued detention of WNBA star Brittney Griner and another former Marine, Paul Wh
elan.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-04/27/21/campaign_images/5f4960638cb4/a-former-marine-was-freed-from-wrong
ful-detention-2-3156-1651095609-1_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/davidmack/brittney-griner-trevor-reed-paul-
whelan-russia">View Entire Post &rsaquo;</a></p>'}, {'title': 'The UK Was Warned This Counterterrorism Program Was A Disaster — But Rolled It Out Anyw
ay', 'link': 'https://www.buzzfeednews.com/article/richholmes/uk-manchester-bombing-counterterrorism-failures', 'pubDate': 'Wed, 13 Apr 2022 13:49:26
-0400', 'image': 'No image found', 'description': '<h1>Revealed: the inside story of how the British government rolled out a dangerously flawed intell
igence-sharing system right as the UK suffered one of its deadliest years from terrorism.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/st
atic/2022-04/13/13/campaign_images/b96d474ef097/the-uk-was-warned-this-counterterrorism-program-w-2-2044-1649857762-6_dblbig.jpg" /></p><hr /><p><a hr
ef="https://www.buzzfeednews.com/article/richholmes/uk-manchester-bombing-counterterrorism-failures">View Entire Post &rsaquo;</a></p>'}, {'title': 'W
orldcoin Promised Free Crypto If They Scanned Their Eyeballs With “The Orb.” Now They Feel Robbed.', 'link': 'https://www.buzzfeednews.com/article/ric
hardnieva/worldcoin-crypto-eyeball-scanning-orb-problems', 'pubDate': 'Tue, 26 Apr 2022 17:44:33 -0400', 'image': 'No image found', 'description': '<h
1>The Sam Altman–founded company Worldcoin says it aims to alleviate global poverty, but so far it has angered the very people it claims to be helping
.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-04/26/17/campaign_images/ac663aaf29dc/worldcoin-promised-free-crypto-if-they-s
canned-th-2-1176-1650995069-65_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/richardnieva/worldcoin-crypto-eyeball-scanning
-orb-problems">View Entire Post &rsaquo;</a></p>'}, {'title': "Ukraine's President Described Nightmarish War Crimes By Russian Forces In Bucha", 'link
': 'https://www.buzzfeednews.com/article/davidmack/ukraine-bucha-zelensky-united-nations', 'pubDate': 'Tue, 05 Apr 2022 18:23:37 -0400', 'image': 'No
image found', 'description': '<h1>President Volodymyr Zelensky used a rare address to the United Nations to describe horrific scenes of death in his c
ountry — and to criticize the Security Council as essentially useless.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-04/5/18/c
ampaign_images/fd962ec378ad/ukraines-president-described-nightmarish-war-crim-2-927-1649183012-21_dblbig.jpg" /></p><hr /><p><a href="https://www.buzz
feednews.com/article/davidmack/ukraine-bucha-zelensky-united-nations">View Entire Post &rsaquo;</a></p>'}, {'title': "It's Cherry Blossom Season And T
he Photos Are Gorgeous", 'link': 'https://www.buzzfeednews.com/article/piapeterson/cherry-blossom-season-photos', 'pubDate': 'Mon, 04 Apr 2022 16:33:4
2 -0400', 'image': 'No image found', 'description': '<h1>How did we get so lucky to live in a world with flowers this pink.</h1><p><img src="https://i
mg.buzzfeed.com/buzzfeed-static/static/2022-04/4/14/tmp/194fa07397f7/tmp-name-2-6819-1649083608-23_dblbig.jpg" /></p><hr /><p><a href="https://www.buz
zfeednews.com/article/piapeterson/cherry-blossom-season-photos">View Entire Post &rsaquo;</a></p>'}, {'title': '“It’s Now Or Never”: The Next Three Ye
ars Are Crucial To Preventing The Worst Impacts Of Climate Change', 'link': 'https://www.buzzfeednews.com/article/zahrahirji/climate-change-report-war
ning-ipcc', 'pubDate': 'Mon, 04 Apr 2022 17:13:59 -0400', 'image': 'No image found', 'description': '<h1>"We are on a fast track to climate disaster,"
 United Nations Secretary-General António Guterres said.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-04/4/17/campaign_images
/c93da27c1ac6/its-now-or-never-the-next-three-years-are-crucial-2-448-1649092435-1_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/ar
ticle/zahrahirji/climate-change-report-warning-ipcc">View Entire Post &rsaquo;</a></p>'}, {'title': 'Russia Has Banned Facebook And Instagram After La
beling Meta\'s Activities “Extremist"', 'link': 'https://www.buzzfeednews.com/article/christopherm51/russia-facebook-instagram-ban-extremist-organizat
ion', 'pubDate': 'Tue, 22 Mar 2022 22:54:46 -0400', 'image': 'No image found', 'description': '<h1>Individuals won’t be held liable for using the two
social media networks, but paying for ads can be regarded as financing an “extremist” group.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static
/static/2022-03/22/22/campaign_images/279f899924ab/russia-has-banned-facebook-and-instagram-after-la-2-982-1647989682-6_dblbig.jpg" /></p><hr /><p><a
href="https://www.buzzfeednews.com/article/christopherm51/russia-facebook-instagram-ban-extremist-organization">View Entire Post &rsaquo;</a></p>'}, {
'title': "Brittney Griner's Detention In Russia Has Reportedly Been Extended For Two More Months", 'link': 'https://www.buzzfeednews.com/article/david
mack/brittney-griner-russia-arrest', 'pubDate': 'Mon, 04 Apr 2022 15:44:41 -0400', 'image': 'No image found', 'description': '<h1>The WNBA star was de
tained at a Moscow airport on drug charges. Supporters fear she\'s being held as a political hostage amid Russia\'s war in Ukraine.</h1><p><img src="h
ttps://img.buzzfeed.com/buzzfeed-static/static/2022-03/18/13/campaign_images/baba97c21d21/brittney-griners-detention-in-russia-has-reported-2-4544-164
7609168-14_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/davidmack/brittney-griner-russia-arrest">View Entire Post &rsaquo;
</a></p>'}, {'title': 'What You’re Feeling Isn’t A Vibe Shift. It’s Permanent Change.', 'link': 'https://www.buzzfeednews.com/article/elaminabdelmahmo
ud/vibe-shift-war-in-ukraine', 'pubDate': 'Fri, 18 Mar 2022 19:25:09 -0400', 'image': 'No image found', 'description': '<h1>I was born during the long
est period of global stability. Now, it appears all of that is fleeting.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/16/2
1/campaign_images/baba97c21d21/what-youre-feeling-isnt-a-vibe-shift-its-permanen-2-1177-1647467700-17_dblbig.jpg" /></p><hr /><p><a href="https://www.
buzzfeednews.com/article/elaminabdelmahmoud/vibe-shift-war-in-ukraine">View Entire Post &rsaquo;</a></p>'}, {'title': 'This Ukrainian Mother Buried Bo
th Of Her Sons Just Six Days Apart', 'link': 'https://www.buzzfeednews.com/article/christopherm51/ukraine-brothers-killed-same-family', 'pubDate': 'We
d, 16 Mar 2022 19:34:18 -0400', 'image': 'No image found', 'description': '<h1>“God takes the very best ones.”</h1><p><img src="https://img.buzzfeed.c
om/buzzfeed-static/static/2022-03/16/19/campaign_images/e7682b2f8deb/this-ukrainian-mother-buried-both-of-her-sons-jus-2-874-1647459253-2_dblbig.jpg"
/></p><hr /><p><a href="https://www.buzzfeednews.com/article/christopherm51/ukraine-brothers-killed-same-family">View Entire Post &rsaquo;</a></p>'},
{'title': 'Russian Oligarch Roman Abramovich Invested At Least $1.3 Billion With US Financiers, Secret Records Show', 'link': 'https://www.buzzfeednew
s.com/article/tomwarren/roman-abramovich-billion-invested-united-states-financiers', 'pubDate': 'Wed, 16 Mar 2022 17:38:25 -0400', 'image': 'No image
found', 'description': '<h1>European governments have frozen the Russian oligarch’s assets, including mansions and a soccer team. But how much he pour
ed into the US has stayed secret.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/16/17/campaign_images/f4fa464b9f8a/russian-
oligarch-roman-abramovich-invested-at-lea-2-597-1647452301-0_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/tomwarren/roman-
abramovich-billion-invested-united-states-financiers">View Entire Post &rsaquo;</a></p>'}, {'title': "A Fox News Camera Operator And A Local Journalis
t Were Killed Covering Russia's War In Ukraine", 'link': 'https://www.buzzfeednews.com/article/davidmack/fox-news-cameraman-pierre-zakrzewski-killed-u
kraine', 'pubDate': 'Wed, 16 Mar 2022 13:31:52 -0400', 'image': 'No image found', 'description': '<h1>Pierre Zakrzewski, 55, and Oleksandra "Sasha" Ku
vshynova, 24, were killed when their vehicle was hit by incoming fire near Kyiv on Monday, according to the network.</h1><p><img src="https://img.buzz
feed.com/buzzfeed-static/static/2022-03/16/13/campaign_images/c5329329f323/a-fox-news-camera-operator-and-a-local-journalist-2-2341-1647437508-4_dblbi
g.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/davidmack/fox-news-cameraman-pierre-zakrzewski-killed-ukraine">View Entire Post &r
saquo;</a></p>'}, {'title': "A Staffer Crashed Russia's Main Evening Newscast With An Anti-War Sign", 'link': 'https://www.buzzfeednews.com/article/da
vidmack/russian-tv-employee-anti-war-protest-live', 'pubDate': 'Tue, 15 Mar 2022 17:12:15 -0400', 'image': 'No image found', 'description': '<h1>“Stop
 the war. Don’t believe the propaganda. They’re lying to you,” Marina Ovsyannikova\'s sign read.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-st
atic/static/2022-03/15/17/campaign_images/1b18fa8feeff/a-staffer-crashed-russias-main-evening-newscast-w-2-553-1647364330-18_dblbig.jpg" /></p><hr /><
p><a href="https://www.buzzfeednews.com/article/davidmack/russian-tv-employee-anti-war-protest-live">View Entire Post &rsaquo;</a></p>'}, {'title': "T
his Russian Newsroom Has Been Cut Off From Its Readers Amid Putin's War. Now It's Asking The World To Help It Report The Truth.", 'link': 'https://www
.buzzfeednews.com/article/skbaer/meduza-crowdfunding-campaign-russia-war-ukraine', 'pubDate': 'Mon, 14 Mar 2022 14:56:59 -0400', 'image': 'No image fo
und', 'description': '<h1>Meduza, a Russian news site based in Latvia, is seeking 30,000 new supporters so that it can continue to deliver independent
 news to millions in Russia.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/11/22/tmp/dd92b7a0b770/tmp-name-2-2649-164703792
1-0_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/skbaer/meduza-crowdfunding-campaign-russia-war-ukraine">View Entire Post
&rsaquo;</a></p>'}, {'title': 'A US Reporter Was Shot Dead While Covering The War In Ukraine', 'link': 'https://www.buzzfeednews.com/article/davidmack
/brent-renaud-reporter-killed-ukraine-war', 'pubDate': 'Mon, 14 Mar 2022 21:49:39 -0400', 'image': 'No image found', 'description': '<h1>White House n
ational security adviser Jake Sullivan said Brent Renaud\'s death was "shocking and horrifying" and pledged that the US would investigate and respond
appropriately.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/14/21/campaign_images/cf8202273a0e/a-us-reporter-was-shot-dead
-while-covering-the-wa-2-492-1647294575-12_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/davidmack/brent-renaud-reporter-ki
lled-ukraine-war">View Entire Post &rsaquo;</a></p>'}, {'title': "How Russia’s Top Propagandist Foretold Putin's Justification For The Ukraine Invasio
n Through This Dramatic Film", 'link': 'https://www.buzzfeednews.com/article/deansterlingjones/russia-yevgeny-prigozhin-ukraine-trump-giuliani-films',
 'pubDate': 'Sat, 12 Mar 2022 18:25:06 -0500', 'image': 'No image found', 'description': '<h1>“Putin’s chef” Yevgeny Prigozhin’s network of state medi
a sites used commissioned Cameo videos from Donald Trump Jr. and Rudy Giuliani to publicize another film that reimagines Russia’s role in the 2016 ele
ction.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/12/1/campaign_images/935d3f7a6aed/how-russias-top-propagandist-foretol
d-putins-just-2-2930-1647048106-5_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/deansterlingjones/russia-yevgeny-prigozhin-
ukraine-trump-giuliani-films">View Entire Post &rsaquo;</a></p>'}, {'title': 'Inside Project Texas, TikTok’s Big Answer To US Lawmakers’ China Fears',
 'link': 'https://www.buzzfeednews.com/article/emilybakerwhite/tiktok-project-texas-bytedance-user-data', 'pubDate': 'Fri, 11 Mar 2022 15:52:52 -0500'
, 'image': 'No image found', 'description': '<h1>TikTok is rebuilding its systems to keep US user data in the US and putting a new US-based team in co
ntrol. But for now, that team reports to executives in China.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/11/15/campaign_
images/935d3f7a6aed/inside-project-texas-tiktoks-big-answer-to-us-law-2-1792-1647013968-23_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednew
s.com/article/emilybakerwhite/tiktok-project-texas-bytedance-user-data">View Entire Post &rsaquo;</a></p>'}, {'title': 'The Biden Administration Has B
een Planning To Tell Mexico That A Trump-Era Policy Could Soon End And Attract More Immigrants To The Border', 'link': 'https://www.buzzfeednews.com/a
rticle/hamedaleaziz/biden-border-plans-title-42', 'pubDate': 'Thu, 10 Mar 2022 22:31:51 -0500', 'image': 'No image found', 'description': '<h1>Returni
ng to prepandemic practices could “seriously strain” border resources and lead to a challenging humanitarian situation in northern Mexico, a draft Dep
artment of Homeland Security document warns.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/10/22/campaign_images/935d3f7a6a
ed/the-biden-administration-has-been-planning-to-tel-2-406-1646951507-8_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/hamed
aleaziz/biden-border-plans-title-42">View Entire Post &rsaquo;</a></p>'}, {'title': "The War In Ukraine Exposes The World's Utter Reliance On Fossil F
uels", 'link': 'https://www.buzzfeednews.com/article/zahrahirji/russia-ukraine-war-fossil-fuels-climate-change', 'pubDate': 'Fri, 11 Mar 2022 00:06:07
 -0500', 'image': 'No image found', 'description': '<h1>“The role of oil and gas in the global economy is very deeply embedded, so any shift is going
to take a long time,” one expert said.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/11/0/campaign_images/23701cca2bb4/the-
war-in-ukraine-exposes-the-worlds-utter-relia-2-575-1646957163-8_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/zahrahirji/r
ussia-ukraine-war-fossil-fuels-climate-change">View Entire Post &rsaquo;</a></p>'}, {'title': 'Bipartisan Bill Aims To Stamp Out Human Rights Abuses A
t Conservation Projects', 'link': 'https://www.buzzfeednews.com/article/tomwarren/house-bill-human-rights-wwf', 'pubDate': 'Thu, 10 Mar 2022 16:56:17
-0500', 'image': 'No image found', 'description': '<h1>Lawmakers say a new bill — prompted by <a href="https://www.buzzfeednews.com/collection/wwfsecr
etwar" target="_blank">a 2019 BuzzFeed News investigatio</a>n — would “signal to the world that the United States demands the highest standards of res
pect for every human life.”</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/10/16/campaign_images/53e695d8152d/bipartisan-bil
l-aims-to-stamp-out-human-rights-ab-2-5840-1646928319-13_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/tomwarren/house-bill
-human-rights-wwf">View Entire Post &rsaquo;</a></p>'}, {'title': 'Russian Troops Pounded The Town Of Irpin. Now They’re Moving Into Ukrainians’ Homes
.', 'link': 'https://www.buzzfeednews.com/article/christopherm51/ukrainians-fleeing-russian-bombing-irpin', 'pubDate': 'Mon, 14 Mar 2022 14:36:48 -040
0', 'image': 'No image found', 'description': '<h1>“For many years, Russians tell us, ‘We’re brothers! We’re one people!’ But look — they’re killing u
s!”</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/14/14/campaign_images/dd92b7a0b770/russian-troops-pounded-the-town-of-irp
in-now-they-2-6808-1647268604-6_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/christopherm51/ukrainians-fleeing-russian-bom
bing-irpin">View Entire Post &rsaquo;</a></p>'}, {'title': '“Our Duty”: Ukrainian Surgeons Are Operating On Russian Soldiers Wounded In Ukraine', 'lin
k': 'https://www.buzzfeednews.com/article/christopherm51/ukraine-surgeons-wounded-russian-soldiers', 'pubDate': 'Mon, 07 Mar 2022 22:25:05 -0500', 'im
age': 'No image found', 'description': '<h1>“I think we should help them but of course sometimes the feeling I have about it is horrible,” Vitaliy, a
surgeon in Kyiv, told BuzzFeed News. “It feels like I’m doing something wrong.”</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-
03/7/16/campaign_images/71d9da805f00/our-duty-ukrainian-surgeons-are-operating-on-russ-2-624-1646670157-1_dblbig.jpg" /></p><hr /><p><a href="https://
www.buzzfeednews.com/article/christopherm51/ukraine-surgeons-wounded-russian-soldiers">View Entire Post &rsaquo;</a></p>'}, {'title': 'Here’s What The
 New Climate Report Says About The Future Of My 1-Year-Old Daughter', 'link': 'https://www.buzzfeednews.com/article/zahrahirji/climate-toddler-future'
, 'pubDate': 'Mon, 07 Mar 2022 16:23:53 -0500', 'image': 'No image found', 'description': '<h1>Not halting global warming, said one expert, “would be
the final, truly unfair thing to do to a generation of kids coming up right now.”</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/202
2-03/7/16/campaign_images/fcad69b55f07/heres-what-the-new-climate-report-says-about-the--2-636-1646670229-10_dblbig.jpg" /></p><hr /><p><a href="https
://www.buzzfeednews.com/article/zahrahirji/climate-toddler-future">View Entire Post &rsaquo;</a></p>'}, {'title': 'A Ukrainian Nuclear Plant Is Now A
War Zone. Here’s What That Means.', 'link': 'https://www.buzzfeednews.com/article/danvergano/ukrainian-nuclear-plant-russia-war-zone', 'pubDate': 'Sat
, 05 Mar 2022 18:29:27 -0500', 'image': 'No image found', 'description': '<h1>“We are in completely uncharted waters,” the head of the International A
tomic Energy Agency said.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/5/18/campaign_images/377c068cc838/a-ukrainian-nucle
ar-plant-is-now-a-war-zone-heres-2-2176-1646504963-12_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/danvergano/ukrainian-nu
clear-plant-russia-war-zone">View Entire Post &rsaquo;</a></p>'}, {'title': 'Facebook And Twitter Have Been Blocked In Russia', 'link': 'https://www.b
uzzfeednews.com/article/sarahemerson/russia-blocks-facebook-twitter', 'pubDate': 'Sat, 05 Mar 2022 04:25:06 -0500', 'image': 'No image found', 'descri
ption': '<h1>Russia’s communications regulator said it blocked Facebook because of “discrimination against Russian media and information resources." T
witter was blocked shortly after.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/4/22/campaign_images/78de2aecb143/facebook-
and-twitter-have-been-blocked-in-russia-2-856-1646433085-8_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/sarahemerson/russi
a-blocks-facebook-twitter">View Entire Post &rsaquo;</a></p>'}, {'title': "Russia's Invasion Is Breaking Up Ukrainian Families And The Photos Are Hear
tbreaking", 'link': 'https://www.buzzfeednews.com/article/davidmack/ukraine-family-farewell-photos-men-stay-fight', 'pubDate': 'Sun, 06 Mar 2022 06:25
:06 -0500', 'image': 'No image found', 'description': '<h1>More than 1.2 million Ukrainians have fled their homeland, but many others are staying to f
ight, leading to emotional scenes at train stations as families say their goodbyes.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2
022-03/4/18/tmp/590adf90ee53/tmp-name-2-715-1646418349-0_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/davidmack/ukraine-fa
mily-farewell-photos-men-stay-fight">View Entire Post &rsaquo;</a></p>'}, {'title': 'Poland’s Top Diplomat In Kyiv Is Pretty Chill About Russia’s Inva
sion Because The City Is “Un-Occupiable”', 'link': 'https://www.buzzfeednews.com/article/christopherm51/poland-ambassador-kyiv-invasion', 'pubDate': '
Fri, 04 Mar 2022 11:25:06 -0500', 'image': 'No image found', 'description': '<h1>“If Russia succeeds here, we are next.”</h1><p><img src="https://img.
buzzfeed.com/buzzfeed-static/static/2022-03/3/21/campaign_images/b8cf3601d87f/polands-top-diplomat-in-kyiv-is-pretty-chill-abou-2-2606-1646344136-25_d
blbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/christopherm51/poland-ambassador-kyiv-invasion">View Entire Post &rsaquo;</a><
/p>'}, {'title': 'Federal Lawmakers Worry Russian Leaders Are Using Crypto To Avoid Sanctions', 'link': 'https://www.buzzfeednews.com/article/saraheme
rson/federal-lawmakers-worry-russian-leaders-are-using-crypto-to', 'pubDate': 'Wed, 02 Mar 2022 21:05:23 -0500', 'image': 'No image found', 'descripti
on': '<h1>US officials continue to scrutinize cryptocurrency markets for their potential role in aiding Russia’s avoidance of sweeping sanctions.</h1>
<p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/2/19/campaign_images/9fc7948d1cfe/federal-lawmakers-worry-russian-leaders-are-usi
ng-2-674-1646250332-13_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/sarahemerson/federal-lawmakers-worry-russian-leaders-a
re-using-crypto-to">View Entire Post &rsaquo;</a></p>'}, {'title': 'Google Maps Blocked Edits After People Falsely Claimed It Was Used to Coordinate R
ussian Air Strikes', 'link': 'https://www.buzzfeednews.com/article/sarahemerson/russia-google-maps-tags-ukraine', 'pubDate': 'Fri, 04 Mar 2022 00:35:3
5 -0500', 'image': 'No image found', 'description': '<h1>Ukrainian-language accounts claimed edits targeted gas stations, schools, and hospitals in ci
ties like Kyiv.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/4/0/campaign_images/1f0102e60ed6/google-maps-blocked-edits-af
ter-people-falsely-cl-2-2926-1646354130-4_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/sarahemerson/russia-google-maps-tag
s-ukraine">View Entire Post &rsaquo;</a></p>'}, {'title': 'Ukrainians Are Desperately Trying To Flee Kyiv As The Russians Advance: “It’s An Absolute N
ightmare”', 'link': 'https://www.buzzfeednews.com/article/christopherm51/ukrainians-flee-kyiv-russian-invasion', 'pubDate': 'Tue, 08 Mar 2022 00:10:52
 -0500', 'image': 'No image found', 'description': '<h1>Thousands of people struggled to board the last trains out of the capital city, forcing famili
es to separate and leave loved ones behind.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/1/20/tmp/fca0bf5b0223/tmp-name-2-
795-1646167136-19_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/christopherm51/ukrainians-flee-kyiv-russian-invasion">View
Entire Post &rsaquo;</a></p>'}, {'title': "Hackers Answered Ukraine's Call For Help. Experts Fear It Isn't Enough.", 'link': 'https://www.buzzfeednews
.com/article/amansethi/ukraine-hacker-cyber-army-russia', 'pubDate': 'Wed, 02 Mar 2022 08:25:05 -0500', 'image': 'No image found', 'description': '<h1
>“Nobody\'s ever crowdfunded or crowdsourced cyber defense before. So we\'re in uncharted territory.”</h1><p><img src="https://img.buzzfeed.com/buzzfe
ed-static/static/2022-03/1/17/campaign_images/fca0bf5b0223/hackers-answered-ukraines-call-for-help-experts-f-2-442-1646157506-4_dblbig.jpg" /></p><hr
/><p><a href="https://www.buzzfeednews.com/article/amansethi/ukraine-hacker-cyber-army-russia">View Entire Post &rsaquo;</a></p>'}, {'title': 'These I
CE Detainees With High-Risk Medical Conditions Fought For Months To Be Released — And They’re Just The Ones We Know About', 'link': 'https://www.buzzf
eednews.com/article/adolfoflores/asylum-seekers-medical-release-delays', 'pubDate': 'Tue, 01 Mar 2022 23:00:52 -0500', 'image': 'No image found', 'des
cription': '<h1>“The lack of medical care is leading to some pretty scary situations for people who are detained there for months and months,” one att
orney said.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/1/23/campaign_images/b2d389565dd8/these-ice-detainees-with-high-r
isk-medical-condit-2-1103-1646175648-25_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/adolfoflores/asylum-seekers-medical-r
elease-delays">View Entire Post &rsaquo;</a></p>'}, {'title': 'The Internet’s Response To Ukraine Has Been Peak Cringe', 'link': 'https://www.buzzfeed
news.com/article/stephaniemcneal/ukraine-memes-tiktok-tweets', 'pubDate': 'Tue, 01 Mar 2022 23:25:06 -0500', 'image': 'No image found', 'description':
 '<h1>From Zelensky thirst traps to <i>Star Wars</i> memes, the collective obsession with virality has led to some embarrassing and insensitive posts.
</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/1/13/campaign_images/fe02b8556a7f/the-internets-response-to-ukraine-has-been
-peak-c-2-1995-1646142696-20_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/stephaniemcneal/ukraine-memes-tiktok-tweets">Vie
w Entire Post &rsaquo;</a></p>'}, {'title': "These Photos Show What It's Like For 500,000 Ukrainians Fleeing Russia's Invasion", 'link': 'https://www.
buzzfeednews.com/article/katebubacz/russia-invasion-ukraine-refugees-photos', 'pubDate': 'Tue, 01 Mar 2022 13:25:07 -0500', 'image': 'No image found',
 'description': '<h1>Ukrainians are fleeing the Russian invasion by foot, train, and car to reach neighboring countries, often enduring a challenging
journey at train stations and borders.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-02/25/21/tmp/13a87ae6faa0/tmp-name-2-1697
-1645823315-31_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/katebubacz/russia-invasion-ukraine-refugees-photos">View Entir
e Post &rsaquo;</a></p>'}, {'title': 'Ukraine Tweeted Its Cryptocurrency Wallet And Got $4 Million In Donations To Help Fight Russia', 'link': 'https:
//www.buzzfeednews.com/article/katienotopoulos/ukraine-has-asked-for-donations-in-crypto-to-help-fight', 'pubDate': 'Mon, 28 Feb 2022 20:45:19 -0500',
 'image': 'No image found', 'description': '<h1>A source who confirmed the government’s fundraiser believed the funds would go to “exterminate as many
 Russian occupants as possible.”</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-02/28/1/campaign_images/40194fda8895/ukraine-tw
eeted-its-cryptocurrency-wallet-and-got-2-1343-1646013240-29_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/katienotopoulos/
ukraine-has-asked-for-donations-in-crypto-to-help-fight">View Entire Post &rsaquo;</a></p>'}, {'title': 'Russia Has Now Been Booted From Eurovision Fo
r Invading Ukraine', 'link': 'https://www.buzzfeednews.com/article/davidmack/eurovision-ban-russia', 'pubDate': 'Fri, 04 Mar 2022 22:26:46 -0500', 'im
age': 'No image found', 'description': '<h1>A number of other European countries had indicated they would not participate in this year\'s popular song
 contest unless Russia was kicked out for its invasion of Ukraine.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/4/22/campa
ign_images/3c92a98e4a98/russia-has-now-been-booted-from-eurovision-for-in-2-879-1646432800-4_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeedn
ews.com/article/davidmack/eurovision-ban-russia">View Entire Post &rsaquo;</a></p>'}, {'title': 'Photos Show How People Around The World Are Respondin
g To Russia Invading Ukraine', 'link': 'https://www.buzzfeednews.com/article/piapeterson/russia-invasion-ukraine-world-protests-photos', 'pubDate': 'F
ri, 04 Mar 2022 21:26:34 -0500', 'image': 'No image found', 'description': '<h1>From Japan to Turkey, people showed up with flags, traditional Ukraini
an clothing, and signs to protest Russia\'s deadly invasion of Ukraine.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/4/21/
campaign_images/78de2aecb143/photos-show-how-people-around-the-world-are-respo-2-728-1646429189-15_dblbig.jpg" /></p><hr /><p><a href="https://www.buz
zfeednews.com/article/piapeterson/russia-invasion-ukraine-world-protests-photos">View Entire Post &rsaquo;</a></p>'}, {'title': 'Russian Troops Have E
ntered Kyiv, Putting Ukraine’s Democratically Elected Government In The Crosshairs', 'link': 'https://www.buzzfeednews.com/article/skbaer/kyiv-russian
-invasion', 'pubDate': 'Fri, 04 Mar 2022 22:15:14 -0500', 'image': 'No image found', 'description': '<h1>“Last time our capital experienced anything l
ike this was in 1941 when it was attacked by Nazi Germany.”</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-03/4/22/campaign_ima
ges/353207b09502/russian-troops-have-entered-kyiv-putting-ukraines-2-846-1646432109-7_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com
/article/skbaer/kyiv-russian-invasion">View Entire Post &rsaquo;</a></p>'}, {'title': 'This Is What It Was Like In Ukraine When Russia’s Attack Change
d Everything', 'link': 'https://www.buzzfeednews.com/article/christopherm51/russian-attack-ukraine-experience', 'pubDate': 'Wed, 09 Mar 2022 09:17:39
-0500', 'image': 'No image found', 'description': '<h1>The blasts shook the walls, illuminated my room even through thick curtains, and jolted me up.<
/h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-02/25/2/tmp/21ce982d7478/tmp-name-2-3286-1645754755-25_dblbig.jpg" /></p><hr /><
p><a href="https://www.buzzfeednews.com/article/christopherm51/russian-attack-ukraine-experience">View Entire Post &rsaquo;</a></p>'}, {'title': "Thou
sands Of Russians, Including Celebrities, Are Risking Being Arrested To Protest Putin's Invasion Of Ukraine", 'link': 'https://www.buzzfeednews.com/ar
ticle/juliareinstein/russian-protest-ukraine-invasion', 'pubDate': 'Mon, 28 Feb 2022 03:25:05 -0500', 'image': 'No image found', 'description': '<h1>T
housands of Russians, including celebrities, protested the deadly invasion of Ukraine on Thursday despite government warnings of "severe punishment."<
/h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-02/24/21/campaign_images/21ce982d7478/russians-are-protesting-their-government-d
espite--2-2710-1645736973-9_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/juliareinstein/russian-protest-ukraine-invasion">
View Entire Post &rsaquo;</a></p>'}, {'title': 'Russia Has Invaded Ukraine, Threatening The Safety Of Millions', 'link': 'https://www.buzzfeednews.com
/article/christopherm51/russia-invades-ukraine', 'pubDate': 'Fri, 25 Feb 2022 17:45:43 -0500', 'image': 'No image found', 'description': '<h1>Russian
shells and missiles hit cities and regions across the country, including many previously untouched by the conflict. “Don’t understand how this can hap
pen in the 21st century,” one Ukrainian civilian seeking safety said.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-02/24/15/t
mp/92552af3bb76/tmp-name-2-2109-1645716858-19_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/christopherm51/russia-invades-u
kraine">View Entire Post &rsaquo;</a></p>'}, {'title': '9 Photo Stories That Will Challenge Your View Of The World', 'link': 'https://www.buzzfeednews
.com/article/piapeterson/photo-stories-feb-19', 'pubDate': 'Tue, 22 Feb 2022 17:35:16 -0500', 'image': 'No image found', 'description': '<h1>Here are
some of the most interesting and powerful photo stories from across the internet.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/202
2-02/22/17/campaign_images/e9954361afcd/9-photo-stories-that-will-challenge-your-view-of--2-8704-1645551310-22_dblbig.jpg" /></p><hr /><p><a href="htt
ps://www.buzzfeednews.com/article/piapeterson/photo-stories-feb-19">View Entire Post &rsaquo;</a></p>'}, {'title': 'Prince Charles Thanked The Queen F
or Giving Her Blessing For Camilla To Become "Queen Consort"', 'link': 'https://www.buzzfeednews.com/article/davidmack/queen-elizabeth-platinum-jubile
e-charles-camilla', 'pubDate': 'Tue, 08 Feb 2022 04:16:09 -0500', 'image': 'No image found', 'description': '<h1>Sunday marks 70 years since Queen Eli
zabeth II assumed the throne. She\'s the first British monarch to ever reach the so-called Platinum Jubilee.</h1><p><img src="https://img.buzzfeed.com
/buzzfeed-static/static/2022-02/6/16/campaign_images/c0ed6941e481/prince-charles-thanked-the-queen-for-giving-her-b-2-13280-1644165706-7_dblbig.jpg" /
></p><hr /><p><a href="https://www.buzzfeednews.com/article/davidmack/queen-elizabeth-platinum-jubilee-charles-camilla">View Entire Post &rsaquo;</a><
/p>'}, {'title': 'Was This Shirt Made With Forced Labor? Hugo Boss Quietly Cut Ties With The Supplier.', 'link': 'https://www.buzzfeednews.com/article
/alison_killing/hugo-boss-removes-esquel-xinjiang-forced-labor', 'pubDate': 'Thu, 03 Feb 2022 15:12:37 -0500', 'image': 'No image found', 'description
': '<h1>Hugo Boss distanced itself from a major clothing manufacturer shortly after <a href="https://www.buzzfeednews.com/article/alison_killing/xinji
ang-forced-labor-hugo-boss-esquel" target="_blank">a BuzzFeed News report</a> on its links to cotton in Xinjiang, which the US has banned.</h1><p><img
 src="https://img.buzzfeed.com/buzzfeed-static/static/2022-02/3/15/campaign_images/c0ed6941e481/was-this-shirt-made-with-forced-labor-hugo-boss-q-2-77
90-1643901152-5_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/alison_killing/hugo-boss-removes-esquel-xinjiang-forced-labor
">View Entire Post &rsaquo;</a></p>'}, {'title': 'These Moving Photos Show The Lives Of Holocaust Survivors Today', 'link': 'https://www.buzzfeednews.
com/article/piapeterson/photos-holocaust-survivors-lives', 'pubDate': 'Fri, 28 Jan 2022 16:33:47 -0500', 'image': 'No image found', 'description': '<h
1>The photo exhibition shows how their lives and legacies are being passed down the generations, reminding us collectively how important it is that th
ey are remembered.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-01/28/16/campaign_images/bd3bd8f298c8/these-moving-photos-sho
w-the-lives-of-holocaust-s-2-2256-1643387622-82_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/piapeterson/photos-holocaust-
survivors-lives">View Entire Post &rsaquo;</a></p>'}, {'title': '7 Photo Stories That Will Challenge Your View Of The World', 'link': 'https://www.buz
zfeednews.com/article/piapeterson/7-photo-stories-that-will-challenge-your-view-of-the-world', 'pubDate': 'Tue, 18 Jan 2022 16:25:10 -0500', 'image':
'No image found', 'description': '<h1>Here are some of the most interesting and powerful photo stories from across the internet.</h1><p><img src="http
s://img.buzzfeed.com/buzzfeed-static/static/2022-01/17/0/campaign_images/a177c9c9d941/7-photo-stories-that-will-challenge-your-view-of--2-2045-1642379
909-0_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/piapeterson/7-photo-stories-that-will-challenge-your-view-of-the-world"
>View Entire Post &rsaquo;</a></p>'}, {'title': 'Facebook’s Spanish-Language Moderators Are Calling Their Work A “Nightmare”', 'link': 'https://www.bu
zzfeednews.com/article/sarahemerson/facebooks-spanish-language-moderators-said-theyre-treated', 'pubDate': 'Fri, 14 Jan 2022 00:48:16 -0500', 'image':
 'No image found', 'description': '<h1>Contractors who moderate Spanish-language content on Facebook said they’ve been forced to come to the office du
ring COVID surges.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-01/13/18/campaign_images/d6add25df1a6/untitled-draft-01132022
-1035-am-2-6626-1642099473-1_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/sarahemerson/facebooks-spanish-language-moderato
rs-said-theyre-treated">View Entire Post &rsaquo;</a></p>'}, {'title': 'Hugo Boss And Other Big Brands Vowed To Steer Clear Of Forced Labor In China —
 But These Shipping Records Raise Questions', 'link': 'https://www.buzzfeednews.com/article/alison_killing/xinjiang-forced-labor-hugo-boss-esquel', 'p
ubDate': 'Wed, 19 Jan 2022 19:44:03 -0500', 'image': 'No image found', 'description': '<h1>Amid rising tensions and the approaching Beijing Olympics,
the US banned Xinjiang cotton last year. But Hugo Boss still took shipments from Esquel, which gins cotton in Xinjiang.</h1><p><img src="https://img.b
uzzfeed.com/buzzfeed-static/static/2022-01/19/19/campaign_images/598a5903de21/hugo-boss-and-other-big-brands-vowed-to-steer-cle-2-7281-1642621437-17_d
blbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/alison_killing/xinjiang-forced-labor-hugo-boss-esquel">View Entire Post &rsaqu
o;</a></p>'}, {'title': 'Novak Djokovic Has To Leave Australia After His COVID Vaccine Exemption Visa Was Canceled', 'link': 'https://www.buzzfeednews
.com/article/davidmack/novak-djokovic-australian-airport-visa-canceled', 'pubDate': 'Thu, 06 Jan 2022 18:25:13 -0500', 'image': 'No image found', 'des
cription': '<h1>The decision means the top-ranked tennis player will likely miss the Australian Open. “They expect to be on the flight back home later
 in the day,” a source told BuzzFeed News.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-01/6/4/campaign_images/71bee5f60e1a/n
ovak-djokovic-has-to-leave-australia-after-his-c-2-1467-1641441849-12_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/davidma
ck/novak-djokovic-australian-airport-visa-canceled">View Entire Post &rsaquo;</a></p>'}, {'title': 'Photos Show A Year Of Catastrophic Events Due To C
limate Change', 'link': 'https://www.buzzfeednews.com/article/piapeterson/climate-change-2021-photos', 'pubDate': 'Wed, 29 Dec 2021 13:21:28 -0500', '
image': 'No image found', 'description': '<h1>We looked back at the year in climate change and the disasters we\'ll be seeing more often as our world
is altered by climate-polluting fossil fuels.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-12/28/20/tmp/120bc7f2b7b9/tmp-name
-2-8257-1640722241-11_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/piapeterson/climate-change-2021-photos">View Entire Pos
t &rsaquo;</a></p>'}, {'title': 'Satellite Images Show Russian Military Forces Keep Massing Near Ukraine’s Border', 'link': 'https://www.buzzfeednews.
com/article/christopherm51/russia-troops-ukraine-border-satellite-photos', 'pubDate': 'Tue, 22 Feb 2022 18:06:40 -0500', 'image': 'No image found', 'd
escription': '<h1>Satellite images provided to BuzzFeed News and a slew of social media videos show that new Russian troops and heavy artillery were m
oved to strategic locations right around Biden and Putin’s virtual summit.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2022-02/22
/18/campaign_images/6558cedccef1/satellite-images-show-russian-military-forces-kee-2-8390-1645553194-1_dblbig.jpg" /></p><hr /><p><a href="https://www
.buzzfeednews.com/article/christopherm51/russia-troops-ukraine-border-satellite-photos">View Entire Post &rsaquo;</a></p>'}, {'title': 'Barbados Ditch
ed The Queen And Immediately Declared Rihanna A National Hero', 'link': 'https://www.buzzfeednews.com/article/davidmack/barbados-republic-rihanna', 'p
ubDate': 'Wed, 01 Dec 2021 17:25:11 -0500', 'image': 'No image found', 'description': '<h1>“May you continue to shine like a diamond."</h1><p><img src
="https://img.buzzfeed.com/buzzfeed-static/static/2021-11/30/15/tmp/1c118f7435c2/tmp-name-2-748-1638286728-5_dblbig.jpg" /></p><hr /><p><a href="https
://www.buzzfeednews.com/article/davidmack/barbados-republic-rihanna">View Entire Post &rsaquo;</a></p>'}, {'title': 'They Arrived At The Pub On Friday
 Night. They Left Monday Morning.', 'link': 'https://www.buzzfeednews.com/article/davidmack/stranded-pub-snow-england', 'pubDate': 'Wed, 15 Dec 2021 2
2:59:02 -0500', 'image': 'No image found', 'description': '<h1>"It was like an adult sleepover!”</h1><p><img src="https://img.buzzfeed.com/buzzfeed-st
atic/static/2021-12/15/22/campaign_images/f3cbb960f29e/they-arrived-at-the-pub-on-friday-night-they-left-2-5983-1639609136-37_dblbig.jpg" /></p><hr />
<p><a href="https://www.buzzfeednews.com/article/davidmack/stranded-pub-snow-england">View Entire Post &rsaquo;</a></p>'}, {'title': 'Clearview AI Is
Facing A $23 Million Fine Over Facial Recognition In The UK', 'link': 'https://www.buzzfeednews.com/article/richardnieva/clearview-ai-faces-potential-
23-million-fine-over-facial', 'pubDate': 'Tue, 30 Nov 2021 02:52:08 -0500', 'image': 'No image found', 'description': '<h1>The provisional decision co
mes after a series of BuzzFeed News investigations revealing widespread and sometimes unsanctioned use of the company’s facial recognition software ar
ound the world.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-11/29/21/campaign_images/a2d22e972074/clearview-ai-is-facing-a-2
3-million-fine-over-fac-2-19607-1638221761-30_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/richardnieva/clearview-ai-faces
-potential-23-million-fine-over-facial">View Entire Post &rsaquo;</a></p>'}, {'title': 'A Chinese Tennis Star Accused A Top Official Of Sexual Assault
. Then She Disappeared.', 'link': 'https://www.buzzfeednews.com/article/davidmack/peng-shuai-missing-mystery', 'pubDate': 'Sat, 20 Nov 2021 02:25:08 -
0500', 'image': 'No image found', 'description': '<h1>Tennis stars are demanding answers about Peng Shuai, whose disappearance has again underscored C
hina’s brutal authoritarianism just months before it hosts the Winter Olympics.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-
11/19/20/campaign_images/534c8657e842/a-chinese-tennis-star-disappeared-after-accusing--2-682-1637355073-15_dblbig.jpg" /></p><hr /><p><a href="https:
//www.buzzfeednews.com/article/davidmack/peng-shuai-missing-mystery">View Entire Post &rsaquo;</a></p>'}, {'title': 'Prevent Catastrophic Climate Chan
ge Or Keep Burning Coal? You Can’t Have Both.', 'link': 'https://www.buzzfeednews.com/article/zahrahirji/climate-change-coal-power-paris-agreement', '
pubDate': 'Fri, 12 Nov 2021 17:17:15 -0500', 'image': 'No image found', 'description': '<h1>"By 2030 in the United States, we won’t have coal,” US Spe
cial Presidential Envoy for Climate John Kerry claimed this week.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-11/12/17/campa
ign_images/45b14bac3a23/prevent-catastrophic-climate-change-or-keep-burni-2-2690-1636737429-17_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfee
dnews.com/article/zahrahirji/climate-change-coal-power-paris-agreement">View Entire Post &rsaquo;</a></p>'}, {'title': 'Amazing Photos Of Airport Reun
ions After The Coronavirus Pandemic Separated Families', 'link': 'https://www.buzzfeednews.com/article/piapeterson/airport-reunions-covid-restrictions
-lifted-photos', 'pubDate': 'Fri, 12 Nov 2021 00:22:38 -0500', 'image': 'No image found', 'description': '<h1>Countries like the US and Australia are
reopening their borders to vaccinated travelers, making for emotional reunions nearly two years in the making at airports around the world.</h1><p><im
g src="https://img.buzzfeed.com/buzzfeed-static/static/2021-11/8/20/tmp/f261884e84bc/tmp-name-2-413-1636403784-8_dblbig.jpg" /></p><hr /><p><a href="h
ttps://www.buzzfeednews.com/article/piapeterson/airport-reunions-covid-restrictions-lifted-photos">View Entire Post &rsaquo;</a></p>'}, {'title': 'Why
 Facebook Shutting Down Its Old Facial Recognition System Doesn’t Matter', 'link': 'https://www.buzzfeednews.com/article/emilybakerwhite/facebook-face
prints-are-the-tip-of-the-biometric-iceberg', 'pubDate': 'Sat, 06 Nov 2021 16:05:41 -0400', 'image': 'No image found', 'description': '<h1>Facebook ju
st made a big deal of shutting down its original facial recognition system. But the company’s pivot to the metaverse means collecting more personal in
formation than ever before.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-11/6/16/campaign_images/8cd06d05b2f5/why-facebook-sh
utting-down-its-old-facial-recogni-2-4310-1636214736-19_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/emilybakerwhite/faceb
ook-faceprints-are-the-tip-of-the-biometric-iceberg">View Entire Post &rsaquo;</a></p>'}, {'title': 'The World Is On Track To Warm 3 Degrees Celsius T
his Century. Here’s What That Means.', 'link': 'https://www.buzzfeednews.com/article/zahrahirji/global-warming-3-degrees-celsius-impact', 'pubDate': '
Thu, 04 Nov 2021 14:31:49 -0400', 'image': 'No image found', 'description': '<h1>Our current coastlines gone. Bangkok underwater. Massive declines in
the fish population. More droughts, downpours, and heat waves.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-10/29/19/campaign
_images/10f527de873a/bad-for-humans-the-world-is-on-track-to-warm-3-de-2-1319-1635537575-13_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeedne
ws.com/article/zahrahirji/global-warming-3-degrees-celsius-impact">View Entire Post &rsaquo;</a></p>'}, {'title': 'How The Pandemic Severed One Of Sou
thern Africa’s Main Economic Lifelines', 'link': 'https://www.buzzfeednews.com/article/markophiri/zimbabwe-cross-border-traders-pandemic', 'pubDate':
'Tue, 09 Nov 2021 00:11:02 -0500', 'image': 'No image found', 'description': '<h1>With few options, some traders have turned to smuggling or sex work.
 “I work with what I have at the moment,” one woman said.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-11/9/0/campaign_images
/58b92f179ceb/how-the-pandemic-severed-one-of-southern-africas--2-821-1636416658-6_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/ar
ticle/markophiri/zimbabwe-cross-border-traders-pandemic">View Entire Post &rsaquo;</a></p>'}, {'title': 'A Data Sleuth Challenged A Powerful COVID Sci
entist. Then He Came After Her.', 'link': 'https://www.buzzfeednews.com/article/stephaniemlee/elisabeth-bik-didier-raoult-hydroxychloroquine-study', '
pubDate': 'Tue, 19 Oct 2021 19:01:03 -0400', 'image': 'No image found', 'description': '<h1>Elisabeth Bik calls out bad science for a living. A feud w
ith one of the world’s loudest hydroxychloroquine crusaders shows that it can carry a high price.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-s
tatic/static/2021-10/19/19/campaign_images/3250f4872991/a-data-sleuth-challenged-a-powerful-covid-scienti-2-833-1634670058-1_dblbig.jpg" /></p><hr /><
p><a href="https://www.buzzfeednews.com/article/stephaniemlee/elisabeth-bik-didier-raoult-hydroxychloroquine-study">View Entire Post &rsaquo;</a></p>'
}, {'title': 'The DOJ Is Investigating Americans For War Crimes Allegedly Committed While Fighting With Far-Right Extremists In Ukraine', 'link': 'htt
ps://www.buzzfeednews.com/article/christopherm51/craig-lang-ukraine-war-crimes-alleged', 'pubDate': 'Mon, 11 Oct 2021 13:09:22 -0400', 'image': 'No im
age found', 'description': '<h1>The probe involves seven men but is centered on former Army soldier Craig Lang, who is separately wanted in connection
 with a double killing in Florida and is fighting extradition from Kyiv.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-10/8/18
/tmp/a50e434c587c/tmp-name-2-486-1633718812-0_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/christopherm51/craig-lang-ukrai
ne-war-crimes-alleged">View Entire Post &rsaquo;</a></p>'}, {'title': 'These Photos Show The Timeless Appeal Of Travel And Tourism', 'link': 'https://
www.buzzfeednews.com/article/piapeterson/photos-travel-photography-history', 'pubDate': 'Thu, 30 Sep 2021 13:16:02 -0400', 'image': 'No image found',
'description': '<h1>“Now that travel has opened up, you can access more places and see more things. Our definition of travel photography has changed.”
</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-09/30/13/campaign_images/038aeec00971/these-photos-show-the-timeless-appeal-of-
travel-a-2-405-1633007759-0_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/piapeterson/photos-travel-photography-history">Vi
ew Entire Post &rsaquo;</a></p>'}, {'title': 'Immigrants Who Escaped The Texas Camp Crackdown Are Facing Another Set Of Dire Circumstances In Mexico',
 'link': 'https://www.buzzfeednews.com/article/adolfoflores/immigrants-mexico-stuck-fear-deportation', 'pubDate': 'Sun, 26 Sep 2021 02:09:15 -0400', '
image': 'No image found', 'description': '<h1>“I’d like to stay here in Mexico, but I’m scared because I don’t have permission to be here,” one immigr
ant told BuzzFeed News. “I don\'t know what to do."</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-09/24/23/tmp/65207c74439c/tm
p-name-2-916-1632527035-9_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/adolfoflores/immigrants-mexico-stuck-fear-deportati
on">View Entire Post &rsaquo;</a></p>'}, {'title': "These Pics Of Angela Merkel Covered In Birds Are Now A Meme And It's Sehr Gut", 'link': 'https://w
ww.buzzfeednews.com/article/davidmack/angela-merkel-birds', 'pubDate': 'Wed, 15 Dec 2021 23:02:29 -0500', 'image': 'No image found', 'description': '<
h1>"Instagram vs. Twitter."</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-12/15/23/campaign_images/f3cbb960f29e/these-pics-of-
angela-merkel-covered-in-birds-are--2-6012-1639609343-0_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/davidmack/angela-merk
el-birds">View Entire Post &rsaquo;</a></p>'}, {'title': 'How A Mission To Turn A Haitian Town Into A Surfing Destination Failed To Live Up To Its Pro
mise', 'link': 'https://www.buzzfeednews.com/article/karlazabludovsky/haiti-surfing', 'pubDate': 'Wed, 22 Sep 2021 00:09:23 -0400', 'image': 'No image
 found', 'description': '<h1>Surfing was a profitable enterprise in Jacmel, as locals rented out boards and hosted lessons. But the project’s recent s
truggles reflect the difficulty of obtaining resources in a country battered by a series of catastrophes.</h1><p><img src="https://img.buzzfeed.com/bu
zzfeed-static/static/2021-09/21/15/campaign_images/4e33950e055b/a-haitian-town-dreams-of-producing-olympic-surfer-2-3050-1632238127-11_dblbig.jpg" /><
/p><hr /><p><a href="https://www.buzzfeednews.com/article/karlazabludovsky/haiti-surfing">View Entire Post &rsaquo;</a></p>'}, {'title': 'Top Scientis
ts At The FDA And WHO Are Arguing Against COVID-19 Booster Shots', 'link': 'https://www.buzzfeednews.com/article/azeenghorayshi/fda-who-booster-shots-
opposition', 'pubDate': 'Wed, 15 Sep 2021 14:38:06 -0400', 'image': 'No image found', 'description': '<h1>In a review published on Monday, the experts
 said the evidence does not show that boosters are needed for the general population.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static
/2021-09/15/14/campaign_images/b0f2592b80f6/top-scientists-at-the-fda-and-who-are-arguing-aga-2-416-1631716682-3_dblbig.jpg" /></p><hr /><p><a href="h
ttps://www.buzzfeednews.com/article/azeenghorayshi/fda-who-booster-shots-opposition">View Entire Post &rsaquo;</a></p>'}, {'title': 'Prince Andrew Has
 Been Served With A Sexual Abuse Lawsuit By Jeffrey Epstein Accuser Virginia Giuffre', 'link': 'https://www.buzzfeednews.com/article/ellievhall/prince
-andrew-served-sexual-assault-lawsuit-giuffre', 'pubDate': 'Fri, 10 Sep 2021 21:15:51 -0400', 'image': 'No image found', 'description': '<h1>The perso
n who served the papers told the court that the first time he tried, Andrew\'s security team said they weren\'t allowed to accept anything court-relat
ed.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-09/10/20/campaign_images/f99c1999996e/prince-andrew-has-been-served-with-a-s
exual-abuse-2-501-1631306521-29_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/ellievhall/prince-andrew-served-sexual-assaul
t-lawsuit-giuffre">View Entire Post &rsaquo;</a></p>'}, {'title': 'He Got Out Of Afghanistan Just In Time. His Family Didn’t.', 'link': 'https://www.b
uzzfeednews.com/article/meghara/afghanistan-kabul-collapse-families-left-behind', 'pubDate': 'Thu, 02 Sep 2021 21:51:59 -0400', 'image': 'No image fou
nd', 'description': '<h1>When Farhad Wajdi left Afghanistan for the US, he assumed he could help his parents get out too. But then everything changed.
</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-08/31/18/tmp/c09b36119bb5/tmp-name-2-405-1630436046-14_dblbig.jpg" /></p><hr />
<p><a href="https://www.buzzfeednews.com/article/meghara/afghanistan-kabul-collapse-families-left-behind">View Entire Post &rsaquo;</a></p>'}, {'title
': 'UN Peacekeepers Fathered Dozens Of Children In Haiti. The Women They Exploited Are Trying To Get Child Support.', 'link': 'https://www.buzzfeednew
s.com/article/karlazabludovsky/haiti-earthquake-un-peacekeepers-sexual-abuse', 'pubDate': 'Tue, 31 Aug 2021 19:21:53 -0400', 'image': 'No image found'
, 'description': '<h1>A landmark ruling in a Haitian court offers some hope to the families seeking child support, but the peacekeeper fathers won’t h
ave to pay unless their home countries step in.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-08/27/19/tmp/1a8523631df5/tmp-na
me-2-583-1630093116-5_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/karlazabludovsky/haiti-earthquake-un-peacekeepers-sexua
l-abuse">View Entire Post &rsaquo;</a></p>'}, {'title': '12 Photo Stories That Will Challenge Your View Of The World', 'link': 'https://www.buzzfeedne
ws.com/article/piapeterson/12-photo-stories-that-will-challenge-your-view-of-the-world', 'pubDate': 'Sun, 29 Aug 2021 22:33:33 -0400', 'image': 'No im
age found', 'description': '<h1>Here are some of the most interesting and powerful photo stories from across the internet.</h1><p><img src="https://im
g.buzzfeed.com/buzzfeed-static/static/2021-08/29/22/campaign_images/fd34ecda5d40/12-photo-stories-that-will-challenge-your-view-of-2-1443-1630276409-5
_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/piapeterson/12-photo-stories-that-will-challenge-your-view-of-the-world">Vie
w Entire Post &rsaquo;</a></p>'}, {'title': 'Working Women In Afghanistan Are Beginning To Navigate Life Under Taliban Rule', 'link': 'https://www.buz
zfeednews.com/article/nishitajha/afghanistan-nurse-hospital-taliban', 'pubDate': 'Fri, 27 Aug 2021 19:42:25 -0400', 'image': 'No image found', 'descri
ption': '<h1>At a hospital in Kabul, terrified patients fled their beds, a new policy bars interactions between men and women, and nurses and doctors
must check in with the Taliban daily.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-08/27/19/campaign_images/557a71866c56/work
ing-women-in-afghanistan-are-beginning-to-nav-2-574-1630093341-2_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/nishitajha/a
fghanistan-nurse-hospital-taliban">View Entire Post &rsaquo;</a></p>'}, {'title': 'These Photos Show The Devastating Aftermath Of The Deadly Kabul Air
port Attack', 'link': 'https://www.buzzfeednews.com/article/kirstenchilstrom/kabul-airport-explosions-aftermath-photos', 'pubDate': 'Fri, 27 Aug 2021
19:59:20 -0400', 'image': 'No image found', 'description': '<h1>At least 13 US service members and an unknown number of Afghan civilians were killed i
n an explosion at an already chaotic airport.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-08/27/19/campaign_images/e95890711
ec3/these-photos-show-the-devastating-aftermath-of-th-2-456-1630094356-13_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/kir
stenchilstrom/kabul-airport-explosions-aftermath-photos">View Entire Post &rsaquo;</a></p>'}, {'title': "London's Famous Notting Hill Carnival Is Canc
eled This Year, But Here's A Look Back At The Party", 'link': 'https://www.buzzfeednews.com/article/piapeterson/photos-london-notting-hill-carnival-ca
nceled', 'pubDate': 'Fri, 27 Aug 2021 01:21:52 -0400', 'image': 'No image found', 'description': '<h1>Looking back at over five decades of joy put on
by the Black British and Caribbean community in London.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-08/26/15/campaign_images
/27b5508b1f22/londons-famous-notting-hill-carnival-is-canceled--2-414-1629991140-19_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/a
rticle/piapeterson/photos-london-notting-hill-carnival-canceled">View Entire Post &rsaquo;</a></p>'}, {'title': 'Police In At Least 24 Countries Have
Used Clearview AI. Find Out Which Ones Here.', 'link': 'https://www.buzzfeednews.com/article/ryanmac/clearview-ai-international-search-table', 'pubDat
e': 'Fri, 27 Aug 2021 19:52:07 -0400', 'image': 'No image found', 'description': '<h1>As of February 2020, 88 law enforcement and government-affiliate
d agencies in 24 countries outside the United States have tried to use controversial facial recognition technology Clearview AI, according to a BuzzFe
ed News investigation.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-08/5/20/campaign_images/5d9697927b4c/untitled-draft-07262
021-1125-am-2-558-1628194743-1_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/ryanmac/clearview-ai-international-search-tabl
e">View Entire Post &rsaquo;</a></p>'}, {'title': 'Foreign UN Staffers Are Evacuating Afghanistan. Local Staffers Say They Have Been Left Behind.', 'l
ink': 'https://www.buzzfeednews.com/article/meghara/un-afghanistan-staffers-taliban', 'pubDate': 'Tue, 24 Aug 2021 21:35:22 -0400', 'image': 'No image
 found', 'description': '<h1>Afghan nationals who work for the UN take on far greater risks for less pay than their international colleagues, and thei
r work leaves them exposed to Taliban reprisals.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-08/24/21/campaign_images/24d9c3
2acdcb/foreign-un-staffers-are-evacuating-afghanistan-lo-2-2367-1629840918-0_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/
meghara/un-afghanistan-staffers-taliban">View Entire Post &rsaquo;</a></p>'}, {'title': '7 Photo Stories That Will Challenge Your View Of The World',
'link': 'https://www.buzzfeednews.com/article/piapeterson/photo-stories-aug-21', 'pubDate': 'Sun, 22 Aug 2021 23:44:02 -0400', 'image': 'No image foun
d', 'description': '<h1>Here are some of the most interesting and powerful photo stories from across the internet.</h1><p><img src="https://img.buzzfe
ed.com/buzzfeed-static/static/2021-08/22/23/campaign_images/c5e6c8cf6460/7-photo-stories-that-will-challenge-your-view-of--2-1260-1629675837-9_dblbig.
jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/piapeterson/photo-stories-aug-21">View Entire Post &rsaquo;</a></p>'}, {'title': 'Pe
ople Who Fled Vietnam Are Reliving Their Trauma Watching The Fall Of Kabul', 'link': 'https://www.buzzfeednews.com/article/skbaer/saigon-kabul-compari
son-vietnam-afghanistan', 'pubDate': 'Tue, 24 Aug 2021 17:21:59 -0400', 'image': 'No image found', 'description': '<h1>"I think about my family, about
 what they’ve been through ... and I think that what\'s going to happen in Afghanistan [is] going to be so much, even worse than what I can imagine."<
/h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-08/20/20/campaign_images/21099efea50a/vietnamese-americans-whose-families-suffer
ed-afte-2-461-1629490562-27_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/skbaer/saigon-kabul-comparison-vietnam-afghanista
n">View Entire Post &rsaquo;</a></p>'}, {'title': 'She Smuggled Women In Kabul To Safety. Now She’s Hiding From The Taliban.', 'link': 'https://www.bu
zzfeednews.com/article/nishitajha/afghanistan-woman-hiding-taliban-blacklist', 'pubDate': 'Sat, 21 Aug 2021 04:57:53 -0400', 'image': 'No image found'
, 'description': '<h1>Though the Taliban have blacklisted Nilofar Ayoubi, she has insisted on speaking out about women’s rights in Afghanistan.</h1><p
><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-08/21/4/campaign_images/c14e421fa17d/she-smuggled-women-in-kabul-to-safety-now-shes-hi
-2-2135-1629521869-7_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/nishitajha/afghanistan-woman-hiding-taliban-blacklist">V
iew Entire Post &rsaquo;</a></p>'}, {'title': 'Big Tech Thought It Had A Billion Users In The Bag. Now It Might Be Forced To Make Hard Choices To Get
Them.', 'link': 'https://www.buzzfeednews.com/article/pranavdixit/big-tech-thought-it-had-a-billion-users-in-the-bag-now-its', 'pubDate': 'Fri, 20 Aug
 2021 18:51:59 -0400', 'image': 'No image found', 'description': '<h1>Long viewed as the world’s biggest market for “the next billion users,” India is
 fast becoming Silicon Valley’s biggest headache.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-08/20/16/campaign_images/55a2c
48b5a20/big-tech-thought-it-had-a-billion-users-in-the-ba-2-410-1629477003-6_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/
pranavdixit/big-tech-thought-it-had-a-billion-users-in-the-bag-now-its">View Entire Post &rsaquo;</a></p>'}, {'title': 'These Photos Of Haiti Show The
 Pain And Turmoil From Back-To-Back Natural Disasters', 'link': 'https://www.buzzfeednews.com/article/kirstenchilstrom/haiti-tropical-storm-photos', '
pubDate': 'Thu, 19 Aug 2021 14:21:54 -0400', 'image': 'No image found', 'description': '<h1>Days after a magnitude 7.2 tremor killed more than 1,400 p
eople, bodies still lie in the streets as officials grapple with the chaos and poor weather.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static
/static/2021-08/17/20/tmp/c74499acc907/tmp-name-2-7018-1629231333-13_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/kirstenc
hilstrom/haiti-tropical-storm-photos">View Entire Post &rsaquo;</a></p>'}, {'title': 'This Is What The Fall Of Kabul To The Taliban Looks Like', 'link
': 'https://www.buzzfeednews.com/article/katebubacz/the-fall-of-kabul-taliban-photos', 'pubDate': 'Tue, 17 Aug 2021 18:45:25 -0400', 'image': 'No imag
e found', 'description': '<h1>Photos show chaotic scenes at the airport and Taliban soldiers patrolling the streets.</h1><p><img src="https://img.buzz
feed.com/buzzfeed-static/static/2021-08/17/18/campaign_images/b587487aa5ab/this-is-what-the-fall-of-kabul-to-the-taliban-loo-2-6832-1629225821-32_dblb
ig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/katebubacz/the-fall-of-kabul-taliban-photos">View Entire Post &rsaquo;</a></p>'},
 {'title': '8 Photo Stories That Will Challenge Your View Of The World', 'link': 'https://www.buzzfeednews.com/article/piapeterson/photo-stories-aug-1
4', 'pubDate': 'Mon, 16 Aug 2021 00:00:58 -0400', 'image': 'No image found', 'description': '<h1>Here are some of the most interesting and powerful ph
oto stories from across the internet.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-08/16/0/campaign_images/c799499a07bf/8-pho
to-stories-that-will-challenge-your-view-of--2-4233-1629072054-3_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/piapeterson/
photo-stories-aug-14">View Entire Post &rsaquo;</a></p>'}, {'title': 'People Have Fallen In Love With This Herd Of Wild Elephants Looking For A New Ha
bitat In China', 'link': 'https://www.buzzfeednews.com/article/piapeterson/wild-elephant-journey-china', 'pubDate': 'Thu, 12 Aug 2021 14:41:48 -0400',
 'image': 'No image found', 'description': '<h1>More than 150,000 people were evacuated from homes in the elephants\' path, but the animals have becom
e local darlings as fans track their progress.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-08/11/19/tmp/aa8c13155dcf/tmp-nam
e-2-2699-1628710722-31_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/piapeterson/wild-elephant-journey-china">View Entire P
ost &rsaquo;</a></p>'}, {'title': 'These Photos Show The Immense Scale Of The Wildfires Ravaging Greece', 'link': 'https://www.buzzfeednews.com/articl
e/kirstenchilstrom/greece-wildfires-photos-destruction', 'pubDate': 'Thu, 12 Aug 2021 00:44:02 -0400', 'image': 'No image found', 'description': '<h1>
Thousands of people, many with injured animals, have been forced to flee the wildfires.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/stat
ic/2021-08/12/0/campaign_images/d4452b8f9f6f/these-photos-show-the-immense-scale-of-the-wildfi-2-3080-1628729037-7_dblbig.jpg" /></p><hr /><p><a href=
"https://www.buzzfeednews.com/article/kirstenchilstrom/greece-wildfires-photos-destruction">View Entire Post &rsaquo;</a></p>'}, {'title': 'Goods Link
ed To A Group That Runs Chinese Detention Camps May Be Ending Up In US Stores', 'link': 'https://www.buzzfeednews.com/article/meghara/china-xinjiang-b
anned-goods-united-states', 'pubDate': 'Fri, 13 Aug 2021 01:22:02 -0400', 'image': 'No image found', 'description': '<h1>A major organization in the r
egion, sanctioned for its “connection to serious human rights abuses against ethnic minorities,” still does business all over the world.</h1><p><img s
rc="https://img.buzzfeed.com/buzzfeed-static/static/2021-08/10/14/campaign_images/83b549cd6ac9/this-is-how-banned-goods-from-chinas-xinjiang-may-2-588
-1628604183-3_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/meghara/china-xinjiang-banned-goods-united-states">View Entire
Post &rsaquo;</a></p>'}, {'title': "Great Britain's First Black Olympic Swimmer Is Hopeful Swimming Caps For Black Hair Will Be Approved For The Next
Games", 'link': 'https://www.buzzfeednews.com/article/ikrd/first-uk-black-olympic-swimmer-caps', 'pubDate': 'Fri, 13 Aug 2021 10:13:50 -0400', 'image'
: 'No image found', 'description': '<h1>“I know a lot of people want to be on the right side of history with this. So I\'m very optimistic that there\
's going to be a positive outcome from it.”</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-08/13/10/campaign_images/c799499a07b
f/great-britains-first-black-olympic-swimmer-is-hop-2-926-1628849625-0_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/ikrd/f
irst-uk-black-olympic-swimmer-caps">View Entire Post &rsaquo;</a></p>'}, {'title': '“It Is Unequivocal”: Humans Are Driving Worsening Climate Disaster
s, Hundreds Of Scientists Said In A New Report', 'link': 'https://www.buzzfeednews.com/article/zahrahirji/ipcc-climate-change-report-2021', 'pubDate':
 'Wed, 11 Aug 2021 14:12:40 -0400', 'image': 'No image found', 'description': '<h1>The highly anticipated United Nations report on climate change deta
ils both the increasingly dire crisis facing the world and what\'s needed to stop it.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static
/2021-08/11/14/campaign_images/17304769824a/it-is-unequivocal-humans-are-driving-worsening-cl-2-2239-1628691156-9_dblbig.jpg" /></p><hr /><p><a href="
https://www.buzzfeednews.com/article/zahrahirji/ipcc-climate-change-report-2021">View Entire Post &rsaquo;</a></p>'}, {'title': 'Yes, Delta Is Scary,
But Europe’s Recent COVID Surges Show That It Can Be Controlled', 'link': 'https://www.buzzfeednews.com/article/peteraldhous/delta-variant-wave-uk-eur
ope', 'pubDate': 'Sun, 08 Aug 2021 22:00:03 -0400', 'image': 'No image found', 'description': '<h1>“The UK and Netherlands should be a counsel against
 despair,” one expert told BuzzFeed News. “We needn’t be fatalistic about the Delta variant.”</h1><p><img src="https://img.buzzfeed.com/buzzfeed-stati
c/static/2021-08/8/21/campaign_images/26f0b93501ee/yes-delta-is-scary-but-europes-recent-covid-surge-2-4205-1628459999-5_dblbig.jpg" /></p><hr /><p><a
 href="https://www.buzzfeednews.com/article/peteraldhous/delta-variant-wave-uk-europe">View Entire Post &rsaquo;</a></p>'}, {'title': "Looking Back At
 Meghan Markle's Last 15 Years For Her 40th Birthday", 'link': 'https://www.buzzfeednews.com/article/piapeterson/meghan-markle-40th-birthday-photos',
'pubDate': 'Wed, 04 Aug 2021 20:11:49 -0400', 'image': 'No image found', 'description': '<h1>Meghan\'s life has changed dramatically over the past dec
ade — here\'s a look back at her epic journey to being a royal.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-07/28/20/tmp/999
8fde51e9f/tmp-name-2-1432-1627504482-26_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/piapeterson/meghan-markle-40th-birthd
ay-photos">View Entire Post &rsaquo;</a></p>'}, {'title': 'Simone Biles Won A Bronze Medal In Her Olympic Return', 'link': 'https://www.buzzfeednews.c
om/article/ikrd/simone-biles-bronze-tokyo', 'pubDate': 'Tue, 03 Aug 2021 16:25:34 -0400', 'image': 'No image found', 'description': '<h1>"I was proud
of myself just to go out there after what I\'ve been through," Biles said afterward.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/
2021-08/3/14/campaign_images/98603ea44d5e/simone-biles-won-a-bronze-medal-in-her-olympic-re-2-8768-1628001341-0_dblbig.jpg" /></p><hr /><p><a href="ht
tps://www.buzzfeednews.com/article/ikrd/simone-biles-bronze-tokyo">View Entire Post &rsaquo;</a></p>'}, {'title': 'Simone Biles Will Compete In The Gy
mnastics Balance Beam Final', 'link': 'https://www.buzzfeednews.com/article/ikrd/simone-biles-balance-beam-mental-health', 'pubDate': 'Mon, 02 Aug 202
1 20:00:53 -0400', 'image': 'No image found', 'description': '<h1>It will be her first appearance since she dropped out of the <a href="https://www.bu
zzfeednews.com/article/adeonibada/simone-biles-olympics-tokyo-team-final-usa?bfsource=relatedmanual" target="_blank">team all-around competition</a> l
ast week, citing her mental health.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-08/2/20/campaign_images/31e9b8af2e80/simone-
biles-will-compete-in-the-gymnastics-balan-2-7647-1627934449-24_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/article/ikrd/simone-b
iles-balance-beam-mental-health">View Entire Post &rsaquo;</a></p>'}, {'title': 'The Uplifting Olympics Content We All Need Right Now', 'link': 'https
://www.buzzfeednews.com/article/kirstenchilstrom/heartwarming-photos-tokyo-olympics', 'pubDate': 'Sat, 31 Jul 2021 03:01:45 -0400', 'image': 'No image
 found', 'description': '<h1>These celebratory moments from the Olympics make me want to cry and cheer.</h1><p><img src="https://img.buzzfeed.com/buzz
feed-static/static/2021-07/30/18/tmp/f2384d0f65b4/tmp-name-2-4365-1627668632-6_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/articl
e/kirstenchilstrom/heartwarming-photos-tokyo-olympics">View Entire Post &rsaquo;</a></p>'}, {'title': 'US Olympic Fencers Wore Pink Masks To Protest A
gainst Their Teammate Accused Of Sexual Assault', 'link': 'https://www.buzzfeednews.com/article/tasneemnashrulla/fencers-pink-masks-alen-hadzic', 'pub
Date': 'Tue, 03 Aug 2021 09:25:41 -0400', 'image': 'No image found', 'description': '<h1>Three men on the US épée team took a stand against their team
mate Alen Hadzic\'s inclusion in the Olympics despite sexual assault allegations against him.</h1><p><img src="https://img.buzzfeed.com/buzzfeed-stati
c/static/2021-07/30/19/campaign_images/42b413a73e4b/us-olympic-fencers-wore-pink-masks-to-protest-aga-2-4463-1627674990-23_dblbig.jpg" /></p><hr /><p>
<a href="https://www.buzzfeednews.com/article/tasneemnashrulla/fencers-pink-masks-alen-hadzic">View Entire Post &rsaquo;</a></p>'}, {'title': 'Gorgeou
s Photos Show What The Last Tokyo Olympics Looked Like In 1964', 'link': 'https://www.buzzfeednews.com/article/piapeterson/tokyo-olympics-1964-photos'
, 'pubDate': 'Sat, 31 Jul 2021 21:25:29 -0400', 'image': 'No image found', 'description': '<h1>Over 50 years ago, Tokyo hosted its first modern Olympi
cs. It looked very different from the games today!</h1><p><img src="https://img.buzzfeed.com/buzzfeed-static/static/2021-07/29/21/campaign_images/a074
b1877fa2/gorgeous-photos-show-what-the-last-tokyo-olympics-2-3203-1627595748-30_dblbig.jpg" /></p><hr /><p><a href="https://www.buzzfeednews.com/artic
le/piapeterson/tokyo-olympics-1964-photos">View Entire Post &rsaquo;</a></p>'}]"""))

    def valid_parse_link_page_test(self):
        self.assertEqual(reader.parse_link_page(news_valid_link),
                         ("Spit, 'disrespect' arrive at Wimbledon as tennis turns ugly"))

    def invalid_parse_link_page_test(self):
        self.assertEqual(reader.parse_link_page(news_invalid_link), 'No description')
