'''
Please do NOT use this for spam, bullying, etc.
By using this script, YOU will take FULL responsibility for anything that happens to ANYONE you use this on and anything you do with this script!.
Additionally, using this script may involve a risk of you being banned and even other risks including but not limited to: being hacked, etc.
Use this script at your own risk!
'''

from selenium import webdriver
# To wait for side load
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Allows us to use keyboard keys
from selenium.webdriver.common.keys import Keys
import time

# Enter in your email for Instagram inside the quotation marks
myemail = ""


# Enter in your password for Instagram inside the quotation marks
mypassword = ""


# friendusernames = ["fragrancenco_"]
friendusernames = ['ms_shiona', 'daponiel_', 'bengeezy05', 'sir_kamcy', 'esteequine', 'jigiman2', 'abbad_ss', 'iamoyediran', 'franklynebere', 'javixy_', 'anee_jkd', 'lynnola_deliveryservices', 'adakolewilliam', 'edidiongb', 'gladchinke', 'okashausmanisah', 'awhitehope', 'sam_igho', 'eyebling_lashes', 'vickayenterprise', 'gbengda', 'hollardusycollection', 'ml_4fashion', 'rocity04', 'indianaprints', 'kel01vin', 'meerahcollections', 'menclassicstories', 'aloot2', 'heelenbones', 'jude_onochie', 'debrah_ni', 'solomon_okla_', '_sleek_ivy', 'sule_gram', 'winifredittah', 'oloye.official', 'bodapal', 'king_dolly_', 'olanrewaju_1010', 'uctru', 'gifted_biz', 'al_mansurr', 'enigmajackson5', 'sir_chuki007', 'iamaimar_', 'oludare.agboola.7', 'abdallahalamin4', 'ummyabullahi22', 'abjocreations', 'ferrarimalik', 'blckjackagency', 'liteskinned_renee', 'titilola_ogunniyan', 'lethalthamannx_2020', 'marysalami04', 'victor_endy', 'lumexbaba1991', 'mhiz_babyb', '25sweetlipz', 'funmi_akintoye', 'omoh_akin', 'merticdesigns_concept', 'jblaql', 'poseidon_wil', 'hair_by_lavicci', 'keem_gege', 'sotonye_69', 's_adam25', 'saifdamrah', 'stanbaba1', 'joke_bolaji', 'toyosi_adebiyi78', 'iam_tina32', 'jamil_jameeel', 'printsdon', 'lloyd2great', 'judith_etimetuk', 'aali__omar', 'asphodel_tulip', '_nenyeee', 'adamuakanimo', 'theoboapea', 'tsbellebeddings_et_al', 'smoothok', '_kanyinsola__', 'simplyclassykiddies', 'mcjblazedwfc', 'hdperfumery', '_________jordan___', 'dorothyshairhub', '_durroothee_', 'mosunmola_a', 'oyeyemi_dominion_adetu2adetule', 'lionandjewelonline', 'sugar__boii', 'lamba_01', 'bakedbyrem', 'kecho78', 'estie202', 'ttoniabiks', 'yahuza_hair_empire', 'oluwatobilobaderinola', 't_yank2000', 'dedec1547', 'forever.pearl5', 'iam_goks', 'beautynfragrancestore', 'sopblisz', 'ummihsan4', 'sumiee__', 'tunde_junaid', 'oliveahanotu', 'benuequeen', 'naccim', 'modupeonitilo', 'baron_fxpro', 'chudy_ctoc', 'gracious_glo', 'minoddyy', 'paulchristopher9', 'monsieurcharle', 'bobbyy.o', 'lakebakare', 'dike_eji_eje_mba', 'outstandinganita', 'azeezah.ibrahim', 'bunmi_olalekanodusanya_', 'zee_perfume_oil', 'justvican', 'mizt.omi', 'mz_mooreoluwa', 'figo9234', 'wiigsbyrez', 'damolafapohunda', 'omoruyiodigie', 'tosynes_accessories', 'bukky1016', 'fahadlawal', 'tomisalau', 'pancakeplug_ng', 'zouks_love', 'joanne_agbam', 'luxurycarsnaija', 'mabraz_trading_company', 'okeybenebs', 'eversmilingglory', 'mr_yousouph', 'jemqween', 'i_am_mermie', 'n.k_lovingherself', 'linda_durkwa', 'jayneassydavid', 'footetish_angel', 'chid_18', 'queen_libby_diva', 'fwanaomi', 'perfume_oils_and_more', 'skinglownaija', 'mistrpeters', 'optimuzprim', 'abdulmumeenandidi', 'momma_zicon', 'diamondwholesalebottles2', '_ladybecks', 'king.shallangwa', 'francc1822', 'fiscophinna01', 'billysgourmetbites', 'ade_daayo', 'dercio.tivane', 'dinoh03', 'ganijay6backupaccount', 'nwaaneke', 'mz_orla', 'ingenious_lawpractitioner', 'house_of_sleeks', '_sandiescent', 'wura_golddy', 'luchyjohn2019', 'ganijay6', 'samuelgodfrey_2020', 'lilylistick12', 'wuragoldy', 'chic_hibu', 'konadu956', 'kvng.rosel', 'babygirlmolly7', 'harxeehpeeta', 'xingxing2021', 'huncho_okes', 'iam_royaltyy', 'adewuyi007', 'ayobamiokla', 'itz_yetty', 'adedokun_jnr1', 'dee_don111', 'priceless_rejoice', 'blesco95.backup', 'chizzbela', 'welmiss2000', 'totalbrideperfumery', 'fikky_fiks', 'maestrodarlingtonxornam10', 'tembeth1', 'kehinde8555', 'annie__hairline', 'lumi_decent', 'melodilisa', 'scentbyoreo', 'mays.fragrances', '64_logistics', 'ziy.closet', 'miraonyebuchi', 'olami_sleek', 'popo_fabrics', 'major.mercy', 'unique_love222', 'sendcityng', 'designer_perfume_mall', 'wholesale_bottles', 'boss__davis1', 'shopbikini.wears', 'pweedieweani', 'alade_honey', 'vaniciaga_', 'rainbow_queeness', 'ope_debss', 'e_faith_196', 'delivery_briskwheel', 'luxeandpearl', 'thitosfragrance', 'triple_henri', 'wardrobeandclosets', 'a_ha256', 'teejuubee', 'ty_daily_store', 'fayisco_jnr', 'mischi_vieous', 'michaelj641', 'ameesweets', 'thelaja', '4kto9k_thriftshoes', 'johnson.omowumi.338', 'detutu__', 'iamwhale_x', 'boss_davis1', 'zarit_hoof', 'damiphilip', 'tytylayomi_07', 'it_isperry', 'slymanraheel', 'tribes_luxury_scents', 'kareh_liyah', 'cazonfoods', 'majesticstylez.biz', 'ajoke_comedy', 'testiheart', 'doyinsbrand', 'almaas_stylishflow', 'fay_scents', 'indianahair_lounge', 'amyluxuryhair', 'damilolafolaazeez', '_wunmii', 'bash1y2k', '19thavenue_ng', 'ajibooh', 'thelittleslipper', 'lusciousseries', 'vida_mariam', 'boujeevendorlists', 'afolashade.afolashade.96', 'thefeet.affairs', 'luvlidoo', 'fragrancebanks', 'theofficialscents', '_rantimi', 'bavic.cosmetic', '__musteey_sherheed', 'mz_ihekaru', 'rosesbedding', 'sophisticatedwristwatch',
                   'sowphs_fragrance', 'perfsbyash', 'theslickclothing', 'renihairline', 'queeneth_vicky', 'shilarr', '5r_concept', 'praiyz_neye', 'relisher_scents', 'yemwatches', 'oilsbyash_', 'shoprave_ng', 'irepitan_', 'malo_soldier', 'magnetique_eventss', 'ofada_koj1', 'hestercowan62', 'hardrockinteriordecorations', 'official_unisce_oni', 'firstgradethriftukaywears', 'korede__o', 'mbbs_bds2020', 'loglash_catering_and_events', 'zobas_hairs', 'paloma_peeter', 'mide.accessories', 'zelumosonwa_', '1kofficebutik', 'iiignacystore', '_opeyemibalogun', 'glowbyash.ng', 'ravishingsurprise_ng', 'annie_chuks_', 'foodabattoir', 'house_of_regeenah', 'p_e_j_u_', 'usman_phina', 'chigoziechinye1', 'blessedotas57', 'aigbovocelina', 'mercyugonick', 'sandilicious4488', 'elizabethfred09', 'lawretta8', 'chibuzonkem27', 'maryebose8', 'princessvickky09', 'feyioluwa75', 'jennyeve09_', 'loveangel9806_', 'pino.pino123', 'cha.chi123', 'anugemaris', 'ifeanyifranca', 'abuunyandu', 'setphenwisdom', 'frank18359', 'joyruth38', 'amaraabigial', 'onyinyechi3746', 'wakeandwalkout', 'nathanprecious8540', 'precikul', 'ezealochibuike', 'veracious_2000', 'nkechi_ruth', 'bathandbodyng', 'foby_oil', 'ife__scents', 'towosworld', 'writer_reo', 'leonsecrets_', 'moyinoluwa_z', 'blissfulessence_', 'yegbraidsby_gabii', 'mr_aktofficial', 'inspiredoutfitss', 'fruitie_delites', 'jacck_logo', 'stephanie__asaah', 'chiefnaa43', 'tz_itunu', 'kessifancy', 'jessyberry28', 'perfectfeetbybb', 'christy_love20', 'aceyemay', 'chinenye____', 'amhani_', 'valerieobaseki', 'mamijay2_', 'patiencejonathan418', 'blessingobim888', 'omoyeemmanuel69', 'charlotteobose', 'chinekezieb', 'lovelytimi987_', 'janeteddy3800', 'celinay551', 'kimanderson0191', 'ifesinachinnenna', 'victoriaebiye_', 'victoriaebiye__', 'preciousigho4', '_fhavourrr', 'sweetestbrenda123',
                   'faithbugatti', 'sorpheeyah_', 'queen_abiodun_ogunnika', 'every_thinghousehold', 'irefoods', 'the14oranges', 'loveangel9806', 'africanweddingvibes', 'worldwideslaykids', 'topup9ja_instagain', 'stebenz_stitches',
                   'symplyogoo', 'lumi_naija', 'motoyosi_b', 'thebudgetavenue', 'faceshield_protects', 'mido_concpet', 'adeyemi_mf', 'drpenny_', 'ogbumarianne', 'roland_abos', 'leonbeddings', 'el_torogram', 'domiwealthcollectionz', 'scarletree', 'dharmpeckins', 'honeysweetbiz', 'i_am_kemmy', 'ayotundee_', 'lo.collections', 'kea_dinayen', 'mzz_meedey', 'm7pay', '_rashida.idris', 'volt_age360', 'timelessfashion__', 'erudite_p', 'tenkobo_logistics', 'simshaevents78', 'anulican', 'zibah_house_of_beauty', 'diamondifeomaaghedo', 'oluke09', 'gabytes_cakes_n_decor', 'liloes_clothing', 'lolacakesnbakes', 'fikayo_x', 'excecutive_beddings', 'beads_by_damselt', 'preach_4teen', 'carolinakrama', 'mzlewah', 'amtosyne', 'nyce_fragrances', 'mrs_doris04', 'thebrandamaka', 'deen_oh', 'temitay1330', 'chadlean', 'angelbrown896', 'dparfumgirl', 'amechi090', 'efeoghene__', 'championsinrelationship', 'hennykarzcouture', 'ayomide_asobele', 'adaorahh_', 'onyi.ok', 'omolola.ojo', 'wakawaka.lifestyle', 'shop_with_mims', 'drinksglam', 'missmadonna', 'adesuwaa_o', 'hafams_', 'disposables_unveil', 'smoothiedaddi', 'lola_dolire', 'q.iyanu', 'daddybrieff', 'eden.jewellers', 'i_schoolboy', 'daveenmakeovers', 'eldoradomedia', 'zibahfoodsangroceries', '__thebottledheaven', 'fabricsbyaduke', 'glitters_ventures', 'payzone_ng', 'dunnis_perfumery', 'forlar_shady', 'cthrinecosmetics', 'stephanie.shaba', '___ajokeade', 'robert_onugha', 'marshnello_', 'ilori_julius', 'teeteenah', 'abenialaaje', 'fenisnature_int', 'shaddyhair_and_wig', 'layo_samuel', 'crunchiemunchies', 'ebiperfume', 'scentgeorgys', 'redolent_collections', '__librae__', 'omosere.joy', 'izzycakeempire', 'zoekainong', 'thesparkleshop43', 'oriflame_ritsywhite', 'adagundamilola', 'petals_n_scents', 'oludipeabimbola', 'man_likejames', 'oghogho.ovonlen', 'dayoaa_', 'tee__olu', 'simmee_lampee', 'olajobi_adedoyin1', 'pelumi325', 'cathe4life', 'fabulouscuttie1', 'nathaliefeisthauer', '_frankah', 'i_am_khaleed', 'amakasgram', 'nyphes_feet', 'pinkandprim', 'pencilworks_designs', 'cheezys_empire', 'nathybanty', '_chinny_xx', 'thrift_hall', 'mzz_riikeh', 'adventureswithoflames', 'african_intelligence_research', 'godstime220gmai', '3pple_a_logistics_', 'frenzydelivery12', 'lagosdigitalmarketingtraining', 'lasheprobeauty', 'ciciekologistics', 'omodolaa', 'scents_abode', 'prospect_clothings', 'lerato7442', 'framedmemoirs.co', 'presh_i', 'clemakpobaro', 'debbybabee', 'itzolexfundz', 'iam_shidah01', 'hasnatt__', 'olatayojulius', 'epic_collection2', 'metamophosis__', 'adorninches', 'nickasbody', 'ahmeed_abdullahi_', 'prettynaomi57', 'chioma9828', 's_arachie', 'mosope_may', 'owobabi456', 'lewascents', 'adigordorathy', 'bibiifit_', 'idrisharunajikandada', 'tumininu.osh', 'dr_maims', 'knaph_stores', 'the.boogeymeme', 'justrice16', 'gunzitzjozzy', 'onyeka_jinna', 'didrabeauty', 'damilola_iyana', 'afolnationwide', 'b.nysc_sdgs',
                   'true.scent', 'hollahyde', 'plantainbuzzlagos', 'style.den', 'theseyiabiodun', 'beclover_designs', 'frost_bel', 'chuviedecorabj', 'debbs__', 'garrick_son7', 'dressyou_style', 'dee_scentsation', 'gloriaayomide', 'folarinhalimata', 'me_rcy4805', 'ada_obi1', 'diuso_dollars', 'halima__al', 'expresspastries', '_.world.art', 'salau_adedayo', 'shiv_ratho', 'mhizgodsonmakinde5', 'asiba.by', 'just_kampalaankaraandsilk', 'adeniyi_adefila', 'ukwuabaoyinye', 'homowumidebby', 'ballyempire2', 'mybride_package', 'pe.ace2609', 'kweentacha', 'adajesus70', 'sentence_obichukwu', 'olamide_ambode', 'abdulazee62', 'oma.2891', 'moustaphayacouba52', 'pngrush', 'yemzy_collectibles', 'vheakys_closet', 'expressurban', 'epheeclara', 'elvidaclothing', 'olukanmio', 'reine_hauwa', 'eridabiraglory', 'ememdelight', 'nouhou458', 'mamependambackemoustapha', 'charlotte_paisley1', 'harrietyeboah92', 'the_real_oreoluwa', 'jhays_hair', 'hybee_fashion_empire', 'lollypoptrendy_weshop4u', 'queenie_mojisola_beauty', 'paulop5600', 'abubakars.sadiq', 'boxerboxer2905', 'lawsilver_event', 'lelea1719', 'natalieempowers', 'spiceandbake', 'kiyah_imperium', 'shitsule', 'adisamusodeeq', 'timzydoll', 'sibonelo961', 'misheckmugare', 'oluwaseyipel', 'for.esther', 'sujobscollections', 'gmpro_x', 'mhizpretty_gift', 'taan1128', 'richeypee', 'obinna905', 'realestatewithbridget', 'dayanjonson', 'ttbeauty_fashion_world', 'ismail_tos_print', 'ziliscute', 'pinky.toyin', 'glitzuplikeyou', 'ssmfashiondesigner', 'happy.alas', 'poweedokskees', '_margpiece', 'splendourz_store', 'tiaazxtraconcept', 'treasure_sugarsecret', 'huchbel', 'rabeemuhd', 'nwrdm10', 'yuyuumaribrahim', 'akinmuleya1', 'martialmaguire', 'kvng_bluetuth', 'adefenwaadebola', 'sorieathullah', 'official_lash2', 'georgetheprogrammer', 'fatima.ajibola', '_shukuru_kassim', '_fadesewa_12', 'josh_meek7', 'cherishayo', 'mivalempire', 'vag1597', 'manuelcosta_24coach', 'gift_boxes.ng', 'pamzfashion', 'deronkes_collectables', 'sena.the.hoodlum', 'shyneluxe_hair', 'digiafragrancestore', 'villagetasteekitchen', 'pona_wears', 'omamalili1', 'dhaymehorn_', 'olalekan5549', 'jpearl_luxury', 'bellastouchstudio', 'zahrahsplace', 'toheebakanni24g', 'edymotors664', 'ajoketbm', 'gorettys1', 'isaacnotey105', 'tony.effiong.71', 'richardkofiampofo', 'trophy_icoacaa', 'princeadediranad', 'beckysalihu', 'dpathfinders_collection', 'benan_stores', 'youngprof1232', 'houseofbeauty2910', 'abimic6464639912', 'olalekan.salawu.902', 'hu.ssain1686', 'sweetsavorbakery', 'konacraft_', 'btfragrance', 'exquisiteasooke', 'giftyglitz', 'ollybeeworld', 'de.cocos_place', 'gracegodwin98', 'pelladebglobalventure', 'oronsayepatience', 'mvlogistics',
                   'milliondollar1', 'jefconfectionerycakes', 'ayorinsola_ventures', 'queen.esthers.empire', 'lavender_wears', 'blessedmynecollectibles', 'skinmattersorganics', 'janetandrew14', 'dteriors', 'dween_essence', 'skinnydipc', 'nkprobeauty', 'ladybees_fashionhouse', 'e_fixbridalstudio', 'finesse_cuisine1', 'nwanat_property',
                   'bouncingevents', 'spencer_collection_', 'in4ucakesgallery', 'in4ucakes', 'prethands_hub', 'joanscollection', 'adejumokeadeyemi', 'justfabapparel', 'sommysvogue', 'epitome_of_edibles', 'lively_sparkzs', 'appetamin', 'mideolaglamaccessories', 'limbra_kollection', 'thacutegeminme_fans', 'gistcouture', 'kingdys_signature', 'prince_berry_', 'poshxpose', 'bally_empire', 'damiebakareempire', 'xquisitefragrances', 'asookebyclasselook', 'the_catena', 'owusubrownlawrence', 'itzyaxzman', 'assoga_aimee', '7943.ellen', 'nice_bed_linen', 'ovuohcommy', 'hannyluv4real', 'ifyautos_', 'skidii_media_pro', 'toyinalugo', 'porchmil', 'baileybryan52', 'ojoko.simileoluwa', 'aso_opeoluwa', 'ogujioforogechi', 'eventsolutionhub', 'nita_2126', 'k_twins_accessories', 'towocare', 'bisbolevents', 'beemash80', 'udochii_', 'chat_martyk', 'dreamlandsolution', 'realstephanie_okere', 'azahs_', 'qorahouse', 'lumieade', 'qorafashion', 'prince_braindan', 'sunmaxtouch', 'crazieoj', 'lauraskitchenng', 'fragrances_junkie', 'yeeteesperfume', 'baakop3network', 'nahoomey', 'nuccyclassic', 'uj_beauty_exploreandcollectios', 'phezzybaby', 'richpearl_ventures', 'mhizsophiapresh', 'mz_mhidey12',
                   'barney.store.ng', 'ekamma', 'ayomidee_joy', 'arashair_', 'muyi_e', 'funmiaffordable_luxury', 'abbie_mhiz', 'debelleza_oilperfumery', 'lola_ajulo', 'fotlotech', 'adamshukurat', 'jummy_fad', 'ghana_professer', 'houseofcriretivity', 'donbasit49', 'nezi_okwu', 'jadinbrown', 'nkemzamara2020', 'ade_kunlegold1', 'newcity_photography', 'avyracollections', 'paulruthgusen', 'sleeklogistics', 'dr_belle_bbq', 'daizy_dazzles_cosmetics', 'mkyrday', 'adukeoflagos', 'medilagfitnessclub', 'busbycakesandevents', 'trendycloset_bydera', 'growmycraft', 'irfansanilawal', 'accessoriesbyfhummie', 'mope_niola', 'oghenekoms', 'oladunni__m', 'rosesstiches', 'kunle882', 'denebcakesandmore', 'fayvo.ufomadu', 'ife_og', 'oluseyiadetolao', 'flavoursogood', 'tahbehlla_wigs', 'cozy_ctrl', 'peejayjnr', 'ireneoflyfe', 'dashobukola', 'pegisisi', 'longrichbusinesshub', 'snstrybe.ng', 'batik_and_indonesian_handmade', 'dinepstore', 'festus.c', 'rosbliscakes', 'olasehindedeborahomolar', 'amaefuleike', 'wakabuzz', 'abbie_tress', 'teachersinnigeria.com.ng', 'dawodusirdi', 'timi_davidz', 'olufemimedics', 'precious_amuta', 'looking4ivy', 'sopuru.sopuru', 'tomiwaadebanji', 'tosa.lisa_empire', 'rahmah_apparel', 'marytosanprint', 'uc_phran6', 'cokeredmond', 'zee_bhee', 'dolufox.o', 'charityifelolorun', 'benny_mora_', '_omojae', 'iphy_nathaniel', 'weddingsnigeria', 'lexyje', 'ufatarena', 'prince_kharter00', 'resistancebands05', 'thriftwithmoi', 'omolara.esan', 'promodelafrica', 'lisemstore', 'jozie_dropshippers', 'naijastreetview', 'chinny4688', 'holuxkid', 'chrxstogram', 'jaycudi52', 'leelattrademark', 'sleekhair___', 'wutoka_creations', 'dave_gatti', 'dance_in_ma_dna', 'rf_accessories', 'portharcourt_trend', 'sinaayo_popoola', 'dr_jaliya', 'derainnykidsclub', 'isiya114', 'hf.cotton.bedsheets', 'akwasi.adu.7564', 'chamccehotels', 'emmanueleze60', 'aqq_innovations', 'kwikeat', 'scents_bylinda', 'papieesmeatro', 'honeyglaze_mua', 'houseofpearl.ng', 'bakkyinfotech', 'georgie007g', 'olohigbe.pd', 'supremesound_ng', 'dirhamforless', 'jaygoodluuck', 'expressmallng', 'frankys_collections', 'young_kore', 'festusojigho1', 'switeebabe', 'yusuff_bolaji', 'oluremi27', 'zikaexpress_logistics', 'physpecial_cakes_more', 'noahotaigo', 'makeupbytomiwa', 'ayinkesvogue', 'cosmeticsbffs.ng', 'health_wellness_empire', 'kunmee_store', 'ultraposhmart', 'officialhouseofduva', 'hf.shoes', 'a_graficz', 'body_mistery', 'milola_closet', 'cakes_by_luscious', 'arinola_asoq', 'alozierita', 'titilope_yeni', 'rihanna2185', 'fosterfaithimagination', 'bigbronaija_live.updates', 'kuku_dcollections', 'ruthyessence_collections', 'tld_femille_hub', 'uniquegee_closet', 'perfectmebody', 'rosepetalz_stores', 'kayanmataguru', 'anyanwusharp', 'jeffery_queen78', 'dassahsthang', 'caramelnaija', 'berrywalterstitches', '_tashasclozet_', 'reuzmaries', 'lionkingdesigns', 'zinnytics', 'toria_bassey', 'tinosaccessories', 'ramaraconcepts', 'iam_ab.kole', 'ibiayebytennie', 'maky_eke', 'legitsales9ja', 'sellitinph', 'khyara_the_first', 'freshdewkids', 'recessmodels', 'sunshine_house_of_fashion', 'klassiq280', 'onetstores', 'pitxestate_realty', 'oyinlola.t', 'techyaccountant', 'peach_place_empire', 'fifi_kidz', 'teemianne_accessoriesnmore', 'ejireclothing', 'l.b.essentials', 'muritalaokponobigmail.com3', 'urbanbylola', 'jkhemanistores', 'deliciousintimacies', 'trendybyghene', 'a_listingsrealty', 'dagrafikr', 'treasure_collectionz', 'madamgeebliss', '_m.n.i.g.g.a_', 'namflix_airings', 'halita_g', 'reen_maps195', 'zainabsaid_', 'dee__scents', 'jencletz_beautyglam', 'techbase_ng', 'eton_beauty_factory', 'f_o_r_t_i_e', 'mbao01', 'hollamarkethub', 'mahyohwah', 'adediran138', 'fortnite_account_codes_seller', '_tosiiin', 'detolas_trove', 'fmcgsearch', 'paragon_boutique61', 'iamkingkhali', 'mhiz_behave', 'stylewithmo_', 'dimplescatering', 'supernatty_1',
                   'sophies_collections', 'supremefabrics1', 'nellyz__glamhair', 'zenoyacollections', 'scentsandbedding', 'loladinkconsult', 'lolaus_dink', 'fashakz_collections', 'd2_minning', 'buyfromjanet', 'peppiekoma_hair', 'ucee_data_service', 'spiritualworkattobati', 'westafricabusinesscentre', 'zeebahworld', 'talktosoft', 'fabricsbymofe', 'kiddies_flair', 'wizz_gadgets', 'romobonyhomes', 'dharmic_gemstones', 'pb_organic_skincare', 'tiffehs_glam', 'attendme.ng', 'mame_collections', 'siotphiri', 'yellowmskincares', 'juicy_gloria', 'oversabi_noise_maker', 'idealpartiess', 'goodiesglamour', 'drealbabe', 'thriftbytigx', 'ritelink', 'fivans_outfit', 'thebox_africa7', 'sandhiesplace_empirefurqueen', 'skittles102988', 'cute_holar', 'kehindeademu', 'petmeeyz_vlog', 'crown__wealth', 'princesskemi2015', 'qindewy', 'kelechi_oriaku', 'jenniemichie', 'aimiki55', 'drelabrith', 'phyl_tymez', 'olatunjeecakes', 'pwetty_leema', 'angiedolie', '__ehi', 'bodywise.essentials', 'peterz.photography', 'dgloss__', 'contentforseo', 'omonyphe', 'hairbyasanwa_', 'hernainz_officiall', 'creatvmarketing', 'mullah666', 'blazeshipping', 'uandnaturepackaging', 'workinhershoes', 'ultrapinkbeauty_shop', 'juliesaccessories_', 'pizzawithmyex', 'ibinabo.t', 'latv.ng', 'excellentfabricsng', 'eniolaoluwanimi.05', 'piniexclusive', 'bags_n_shoes_', 'seunegbewunmi', 'ogun_market_hub', 'pricesslessqueen', 'hairguruafrica', 'slim_lily1', 'bukkygroove', 'yokotofoods', 'mathewtamy', 'rocamfoundation', 'elyonson', 'hormourtawla', 'eden_dena', 'cashlog0000', 'nevidablog', 'sensationalbitez', 'ellen_gurule', 'simi_luxury', 'uniqueemporium.ng', 'wigsbytee_', 'vanpiranc_shot', 'evastravelsolutions', 'adopretty_makeover', 'giftys_place', 'hairbytemmy', 'kingsley.aniegbo', '_just.opson_', '4sme.com.ng', 'xtrovarts', 'kumbayaafrica', 'stacy_white4u', 'xteemstudios', 'celestialpreneurshub', 'cake_by_jenny', 'product_reviews_store', 'meraki_tv',
                   'mizpah_fm', 'onenineja', 'the_print_guru', 'beebah_fabrics', 'pearlsapparelng', 'bimladwears83', 'everything_bimmy', 'uc_morezphones', 'houzofjazz', 'pennek_nigeria', 'ay_agbaje', 'adrielladimples', 'coldcubeice', 'july5th_empire', 'zadoya_makeovers', 'coreopscleaners', 'gracies_fashion_empire', 'cottsframeng', 'odunayoelisa', 'chinawholesales_', 'martcribz', 'cheetah2730', 'fragrancetips', '_taayo', '_abebii_', 'tonbratoms', 'abiolaayomikun', 'lase_moye', 'the_iseoluwa', '43forex_academy', 'thedreammonetizer', 'abbycutiee', 'lady.p_clothing', 'bestpricekiddiesstore', 'tboygabzy', 'pmndifon', 'rukkybellaz', 'mz_cutiebear', 'ezehebuka48gmi', 'tinuade_ayomide', 'amologistics', 'dayveed_xx', 'classiekiddies', 'irene_lanez', 'its_niphe', 'rolyguy', 'jhnsinos', 'officialclems', 'meenahs_palace', 'gadgetsandco_', 'itunuy', 'agathalegal', 'caramella____', '_gaming_bruder_', 'brideandmaidsfactory', 'six_25butik', 'gcseducation', 'olusolaamusan', 'iconic_faces_ng', 'jamie_watch', 'ldm_cosmetics', 'ibrahimisa2828', 'mj_kids_apparel', 'joyslizzy', 'emillie_jayne_bespoke', 'demisyhair', 'marygolding85', 'dorothy_jaja', 'ayoarigbs', 'lyr_accessories', 'henriblog', 'thehustlespiceking', 'houseofdivas.ng', 'nellz_exclusive', 'southsouth_vibes', 'chevonne_cosmetics', 'ifuskin.solutions', 'anthurium_hotel', 'sakaila_hairs', 'morena_jay', 'affordable_fab', 'ivannas.collections', 'sales_curve', 'elenacova_', 'snoopiewears', 'the_niceshopping', 'kokz_collection', 'souvenirsbygold', 'dannabeauty_', 'dollyqueeneebeautypro', 'unikredoil', 'faith_ezennaya', 'ogawilliamswaltd', 'jesseytouch', 'boluwxtife', 'klasick_beads', 'hayjay_organics', 'cupideventsng', 'tarila_ajuesi', 'zeeky_cakes', 'blessingezaka', 'ozegberic', 'dr_snowyt', 'ewardunni', 'kelsey_makeovers', 'aomintegrated', 'strutinlanez', 'dbookplace', 'becky_bbeauty', 'lagosexpo', 'aquaklens', 'tboclothings', 'celemat', 'obeyaluminium8', 'vicci_bakare', 'brightlandproperties', 'asmonpeters', 'fematechgadget_', 'king_kekere', 'glamourstores_', 'sekina_adeyemi', 'hasmet_dayi', 'yetundedada74', 'iceyfashionstore', 'officialbusolami', 'youngboss_fanpage_', 'educated_thuggg', 'chinawholesale_kiddiesitems', 'iamtosintaylor', 'dbautohire', 'gabbyjay20', 'orelovesoreo', 'jou.glam', 'ebookmentor', 'regeenah_dee', 'china_importexpert', 'hizzangelradow', '_nenye__',
                   'chynonxo', 'gimplexlogistics', 'im_chichii', 'beepmedia47', 'iamelegant01', 'gbeminola', 'cozydecor.ng',
                   'totallytrendy_by_lammy', 'damigoldclothings', 'oomochioo666', 'oliviadavidsluxuries', 'sweetgenre_cakes', 'gamebreakerr', 'royalbeddingnaija', 'r_e_a_l_s_a_m', 'royalvenice', 'mappipgadgets', 'favygiant', 'sugarcyril', 'ceejayikpeze', 'olawayee', 'ransomeautos', 'yhumiesaxophonist', 'minuelfaleti', 'femiadedeji', 'clameliaservices', 'f__ua__d', 'roysavivastore', 'officialnictv', 'choiceassistantltd', 'amaafashion', 'princessroseyb', '_amaraaaa_', 'omobolafad', 'alayoni_adee', 'prettyberri', 'sales_connect', 'tatahairsolutions', 'futuresoftng', '_modemartins', 'wolejunior', 'bidsglam', 'titan_apparels', 'owanbe_vendors', 'otse__', 'naoslay', 'feragostyle', 'duro_teemy', 'mrbanks_official', 'allure_express', 'luisz5th', 'akes_hub', 'teemsglobal', 'busayos_place', 'walitees', 'decluttercabin', 'vivian_nwosu', 'naturelover__007', 'bassetclothings', 'greenlottong', 'kleo_products', 'sunshinepantryhouse', 'samwelgachuhikaimba', 'temitope_fadare', '_hennabyhafsah', 'topsecret_hairplanet', 'veedahlia', 'hephzibahs_collections', 'morgans_stores', 'tiri.ng', 'thewears_mall', 'chi__ora', 'macedigital', 'niklar_world', 'onpointwristwatches', 'jaydizworld', 'novakids_', 'undress_stores', 'tanelaerrands', 'atad_luxury', 'deevapreneur', 'styleswitch.ng', 'allroundcargocompany', 'deedees_collection_']      # Enter in the username of the recipient inside the quotation marks! To send this to mutiple users, seperate users by commas! Ex)  friendusernames = ["@friend1", "@friend2", "@friend3"]

numoftimes = "1"             # Enter in the number of times you would like to send the message to the recipient Ex) "2"

# The message being sent
messages = ["Hello and good day dear follower / potential customer. This is FragranceNco _\n", "Our previous account(@fragragrancenco)was hacked, and we may not be able to retrieve it.\n", "Kindly follow this new one(@fragrancenco_).\n", "We would love you to have you back, and we would also love you to help us build our page back from the scratch.\n",
            "That’s why every little follow matters.\n", "Thank you for staying with us so far, let’s do it again.\n", "We would be posting more so you can see new stock and enjoy your shopping journey.\n", "Please Disregard any fraudulent message from our previous page(@fragrancenco).\n", "The username on that old page now is (@nicole_andrea_fx__)\n", "Please do not under any circumstance, pay money to anyone with that name or from that account to avoid getting scammed.\n", "Love, FragranceNco.\n"]


# Step 4 of the installations instructions
# PATH = "" #path to where the driver is 


PATH = "D:\drivers\chromedriver_win32\chromedriver.exe" ## an example

driver = webdriver.Chrome(PATH)
# driver = webdriver.Chrome(executable_path=r'C:/path/to/chromedriver.exe') //an example

offset = 110
MAX_RANGE = 50 # instagram seems to limit to about 110 messages so you can change it from 50 to 110

url = "https://www.instagram.com/"
driver.get(url)

try:
    try:
        # Waits for the login box to appear on the webpage
        usernamebox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        # Login to Instagram
        usernamebox.send_keys(myemail)
        passwordbox = driver.find_element_by_name('password')
        passwordbox.send_keys(mypassword)
        loginbutton = driver.find_element_by_css_selector('.Igw0E')
        loginbutton.click()
        print("Logging in")
    except:
        print("Could not login!")

    try:
        dmbtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xWeGp')))
        dmbtn.click()
    except:
        print ("Could not find or click the direct message button")

    try:
        notificationsnotnow = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.HoLwm')))
        notificationsnotnow.click()
    except:
        print ("Could not click not now on the notifications pop up!")

    length = len(friendusernames)
    for index in range(MAX_RANGE):
        count = offset + index
        if count < length:
            friendusername = friendusernames[count]
            try:
                searchuser = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.EQ1Mr')))
                searchuser.click()
            except:
                print ("Could not click on the new message button!")
            try:
                searchuserbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.j_2Hd')))
                searchuserbox.send_keys(friendusername)
            except:
                print ("Could not find the enter username box!")

            try:
                # time.sleep(5)
                time.sleep(2)
                # firstuser = driver.find_element_by_css_selector('.HVWg4')
                firstuser = driver.find_element_by_css_selector('.dCJp8 ')
                # print(firstuser)
                firstuser.click()
            except:
                print("Could not click on the first user!")

            try:
                pressingnext = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rIacr')))
                pressingnext.click()
            except:
                print ("Could not press \"Next\"!")

            try:
                messagebox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.focus-visible')))
                messagebox.click()
            except:
                print ("Could not find the text box!")

            try:
                # Finds the text box
                textbox = driver.find_element_by_css_selector('.focus-visible')
            except:
                print("Could not find the text box!")

            try:
                # Sends the message
                for i in range(int(numoftimes)):
                    for message in messages:
                        textbox.send_keys(message)
                        textbox.send_keys(Keys.RETURN)
                    # textbox.send_keys(message1)
                    # textbox.send_keys(Keys.RETURN)
                print(f"Completed {count + 1} users")
            except:
                print("Error sending the message!")

except:
    print("An error has occurred")
    time.sleep(1)
    driver.quit()
