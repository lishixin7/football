import js2xml
import requests, re
from lxml import etree
from numpy import integer
from scrapy.selector import Selector

# from selenium import webdriver # 导入webdriver包
# driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver")  # 找一个合适版本的IEDriver

data = """"
<!DOCTYPE html>
<html lang="en" xmlns:wb="http://open.weibo.com/wb">
<head>
    <meta charset="utf-8">
    <title>勒沃库森 v 尤文图斯（现场数据 2019/12/12） - DS足球</title>
    <link rel="shortcut icon" href="/favicon.ico">
    <meta property="qc:admins" content="1642520177643251156375"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=3.0, user-scalable=1">
    <link rel="stylesheet" href="/assets/css/app.min.css?_=248">
    <script src="/assets/vendor/modernizr/modernizr.js"></script>
    <script type="text/javascript" src="/assets/js/jquery.min.js"></script>
    <script type="text/javascript" src="/assets/js/fav.js?_id=6"></script>
    <script type="text/javascript" src="/assets/js/new_signup.js?_id=40"></script>
    <script type="text/javascript" src="/assets/js/jquery.validate.min.js"></script>
    <script>
        var DS_domain_config = {
            'is_live_domain': 0,
            'cookie_domain': '.dszuqiu.com',
            'root_domain': '//www.dszuqiu.com'
        };
    </script>
    <script type="text/javascript" src="/assets/js/comment.js?_=31"></script>
    <script>
        var _hmt = _hmt || [];
        (function () {
            var hm = document.createElement("script");
            hm.src = "//hm.baidu.com/hm.js?a68414d98536efc52eeb879f984d8923";
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(hm, s);
        })();
    </script>
    <script>var is_en = 0;</script>
    <meta name="baidu_ssp_verify" content="f295905cd1eff2ed30979a429504cb6b">

</head>
<body>
<div class="wrapperV2 ">
    <nav class="topNavBar" id="topBar">
        <div class="row">
            <div class="small-12 columns">
                <div class="topNavBarInner">
                    <dl class="sub-nav topNav">
                        <dd>
                            <a class="logo" href="//www.dszuqiu.com/" style="padding:14px 0 10px 0;">足球比分直播</a>
                        </dd>
                        <dd><a href="//live.dszuqiu.com">即时比分</a></dd>
                        <dd><a href="//live.dszuqiu.com/corner">角球比分</a></dd>
                        <dd class="dsHasDropdown ">
                            <a data-dropdown="diaryDropdown" aria-controls="diaryDropdown" aria-expanded="false"
                               data-options="is_hover:true; hover_timeout:100; align:left;"
                               onclick="window.location='//www.dszuqiu.com/diary'">比赛日程</a>
                            <ul id="diaryDropdown" class="f-dropdown topNavBarDropdown" data-dropdown-content
                                aria-hidden="true" tabindex="-1">
                                <li><a href="//www.dszuqiu.com/jczq">竞彩足球</a></li>
                                <li><a href="//www.dszuqiu.com/bjdc">北京单场</a></li>
                            </ul>
                        </dd>
                        <dd><a href="//www.dszuqiu.com/data">足球赛事</a></dd>
                        <dd class="dsHasDropdown ">
                            <a data-dropdown="newsDropdown" aria-controls="newsDropdown" aria-expanded="false"
                               data-options="is_hover:true; hover_timeout:100; align:left;"
                               onclick="window.location='//www.dszuqiu.com/articles'">足球资讯</a>
                            <ul id="newsDropdown" class="f-dropdown topNavBarDropdown" data-dropdown-content
                                aria-hidden="true" tabindex="-1">
                                <li><a href="//www.dszuqiu.com/articles/lottery">竞彩专栏</a></li>
                                <li><a href="//www.dszuqiu.com/articles/expert"
                                       style="letter-spacing: 6px; text-align:center !important; margin-left:5px;">专家号</a>
                                </li>
                            </ul>
                        </dd>
                        <dd class="dsHasDropdown"><a href="//www.dszuqiu.com/live" data-dropdown="videoDropdown"
                                                     aria-expanded="false"
                                                     data-options="is_hover:true; hover_timeout:0; align:left;"
                                                     onclick="window.location='//www.dszuqiu.com/live'">视频直播</a>
                            <ul id="videoDropdown" class="f-dropdown topNavBarDropdown" data-dropdown-content
                                aria-hidden="true" tabindex="-1">
                                <li><a href="//www.dszuqiu.com/video">视频集锦</a></li>
                                <li><a href="//www.dszuqiu.com/record">录像回放</a></li>
                            </ul>
                        </dd>
                        <!--<dd><a href="//www.dszuqiu.com/photos">足球图库</a></dd>-->
                        <dd><a href="//www.dszuqiu.com/app">手机APP</a></dd>
                        <dd class="dsHasDropdown"><a href="//www.dszuqiu.com/wemedia" data-dropdown="tuanDropdown"
                                                     aria-expanded="false"
                                                     data-options="is_hover:true; hover_timeout:0; align:left;"
                                                     onclick="window.location='//www.dszuqiu.com/wemedia'"
                                                     rel="nofollow">我的专家号</a>
                            <ul id="tuanDropdown" class="f-dropdown topNavBarDropdown" data-dropdown-content
                                aria-hidden="true" tabindex="-1" style="margin-left:87px;">
                                <li><a href="//www.dszuqiu.com/user/tuan_apply" rel="nofollow"
                                       style="letter-spacing: 9px; text-align:center !important; margin-left:5px;">专家团</a>
                                </li>
                            </ul>
                        </dd>
                    </dl>
                    <div class="topBarRight">
                        <ul>
                            <li class="topBarAccount">
                                <a class="topBarAccountLink">
                                    <img src="https://s.besget.com/profile/200/419899df1ad47ab39e456311dd18e603.jpg"
                                         class="photo"/>
                                    <strong>
                                        wwwwwyb <i class="fa fa-angle-down"></i>
                                    </strong>
                                </a>
                                <ul id="acountDrop" style="z-index: 1089 !important;">
                                    <li class="text-center"><a href="//www.dszuqiu.com/user"><i
                                            class="fa fa-user f18 VM"></i> 用户中心</a></li>
                                    <li class="text-center"><a href="//www.dszuqiu.com/user/fav/fav_races"><i
                                            class="fa fa-star f18 VM"></i> 我的关注</a></li>
                                    <li class="text-center"><a href="//www.dszuqiu.com/logout"><i
                                            class="fa fa-sign-out f18 VM"></i> 安全退出</a></li>
                                </ul>

                            </li>

                        </ul>
                    </div>
                    <div class="topBarNavSearch">
                        <form class="form-horizontal" id="data_search" role="form"
                              action="//www.dszuqiu.com/data/search" method="get">
                            <input type="text" class="searchField" id="search_name" name="search_name"
                                   placeholder="搜索你喜欢的球队、赛事"/>
                            <span class="topBarNavSearchBt"><i class="fa fa-search"></i></span>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </nav>

    <!-- main start -->
    <main class="main analysisMain">

        <script type="text/javascript" src="/assets/vendor/jquery.cookie/jquery.cookie.js"></script>
        <script>
            $(document).ready(function () {
                var enable_corner_flag = $.cookie('enable_corner_flag');
                if (enable_corner_flag == null) {
                    $(".timeLineCorner").show();
                    $(".timeLine").addClass('cornerTimeLine');
                }
            });
        </script>

        <div class="analysisWrapper">
            <div class="row">
                <div class="small-12 columns">
                    <div class="row">
                        <div class="small-10 small-centered columns">
                            <h3 class="dsBreadcrumbs" style="left:0;"><span>您当前的位置： </span>
                                <a href="//www.dszuqiu.com/">首页</a> <i class="fa fa-angle-right" aria-hidden="true"></i>
                                <a href="//www.dszuqiu.com/data">足球赛事</a> <i class="fa fa-angle-right"
                                                                             aria-hidden="true"></i>
                                <a href="//www.dszuqiu.com/league/117">欧洲冠军联赛</a> <i class="fa fa-angle-right"
                                                                                     aria-hidden="true"></i> 勒沃库森 vs
                                尤文图斯
                            </h3>
                            <div class="analysisHead">
                                <div class="row">
                                    <div class="small-2 columns text-center">
                                        <div class="analysisTeamImg">
                                            <img src='https://s.besget.com/team/b/2681.png'/></div>
                                        <h3 class="analysisTeamName red-color"><a href="/team/481"
                                                                                  class="red-color font-bold"
                                                                                  target="_blank">勒沃库森</a></h3>
                                    </div>
                                    <div class="small-6 small-offset-1 columns text-center" id="race_part">
                                        <div class="analysisHeadRaceInfo MBTitle">
                                            <div class="analysisHeadData">
                                                <span class="VM"><img src="/assets/images/event/cd.png" width="14"
                                                                      class="VM MT-3"> 良好</span>
                                                <span class="VM"><img src="/assets/images/event/tq.png" width="14"
                                                                      class="VM MT-3"> 良好</span>
                                                <span class="analysisRaceTime" style="display: inline-block;"> 2019/12/12 04:01
                                            <a race-new-fav-id="701326" class="analysisFav  "><i class="fa fa-star"></i><i
                                                    class="fa fa-star-o"></i></a>                                        </span>
                                            </div>
                                            <div class="analysisHeadScore">
                                                <div class="row">
                                                    <div class="small-4 columns text-right"><h3>0</h3></div>
                                                    <div class="small-4 columns text-center">
                                                        <span class="time">全</span>
                                                        <p class="analysisHeadScoreCorner">
                                                            6 <img src="/assets/images/icon_corner.png" alt="角球"
                                                                   width="16" class="MT-3"> 2 </p>
                                                    </div>
                                                    <div class="small-4 columns text-left"><h3>2</h3></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="timeLine MBTitle" id="race_timeLine">
                                            <div class="timeLineBg1"></div>
                                            <div class="timeLineBg2" style="width:100%;"></div>
                                            <span class="timeLineL5min" style="left:5.6%;"></span>
                                            <span class="timeLineL10min" style="left:11.1%;"></span>
                                            <span class="timeLineL5min" style="left:16.7%;"></span>
                                            <span class="timeLineL10min" style="left:22.2%;"></span>
                                            <span class="timeLineL5min" style="left:27.8%;"></span>
                                            <span class="timeLineL10min" style="left:33.3%;"></span>
                                            <span class="timeLineL5min" style="left:38.9%;"></span>
                                            <span class="timeLineL10min" style="left:44.4%;"></span>
                                            <span class="timeLineL5min" style="left:50%;"></span>
                                            <span class="timeLineL10min" style="left:55.7%;"></span>
                                            <span class="timeLineL5min" style="left:61.1%;"></span>
                                            <span class="timeLineL10min" style="left:66.7%;"></span>
                                            <span class="timeLineL5min" style="left:50%;"></span>
                                            <span class="timeLineL10min" style="left:66.7%;"></span>
                                            <span class="timeLineL5min" style="left:72.2%;"></span>
                                            <span class="timeLineL10min" style="left:77.8%;"></span>
                                            <span class="timeLineL5min" style="left:83.3%;"></span>
                                            <span class="timeLineL10min" style="left:88.9%;"></span>
                                            <span class="timeLineL5min" style="left:94.4%;"></span>
                                            <span aria-haspopup="true" class="timeLineCorner" title="17' - 第1角球 - 勒沃库森"
                                                  style="left:18%;z-index:100; display:none;"><img
                                                    src="/assets/images/event/timeline-corner-h-7.png" class=""
                                                    alt="角球"/></span> <span aria-haspopup="true" class="timeLineCorner"
                                                                            title="18' - 第2角球 - 勒沃库森"
                                                                            style="left:20%;z-index:101; display:none;"><img
                                                src="/assets/images/event/timeline-corner-h-7.png" class=""
                                                alt="角球"/></span> <span aria-haspopup="true" class="timeLineCorner"
                                                                        title="34' - 第3角球 - 勒沃库森"
                                                                        style="left:37%;z-index:102; display:none;"><img
                                                src="/assets/images/event/timeline-corner-h-7.png" class=""
                                                alt="角球"/></span> <span aria-haspopup="true" class="timeLineCorner"
                                                                        title="41' - 第4角球 - 勒沃库森"
                                                                        style="left:45%;z-index:103; display:none;"><img
                                                src="/assets/images/event/timeline-corner-h-7.png" class=""
                                                alt="角球"/></span> <span aria-haspopup="true" class="timeLineCorner"
                                                                        title="44' - 第5角球 - 勒沃库森"
                                                                        style="left:48%;z-index:104; display:none;"><img
                                                src="/assets/images/event/timeline-corner-h-7.png" class=""
                                                alt="角球"/></span> <span aria-haspopup="true" class="timeLineCorner"
                                                                        title="53' - 第6角球 - 尤文图斯"
                                                                        style="left:58%;z-index:105; display:none;"><img
                                                src="/assets/images/event/timeline-corner-g-7.png" class=""
                                                alt="角球"/></span> <span aria-haspopup="true" class="timeLineCorner"
                                                                        title="56' - 第7角球 - 勒沃库森"
                                                                        style="left:62%;z-index:106; display:none;"><img
                                                src="/assets/images/event/timeline-corner-h-7.png" class=""
                                                alt="角球"/></span> <span aria-haspopup="true" class="timeLineCorner"
                                                                        title="74' - 第8角球 - 尤文图斯"
                                                                        style="left:82%;z-index:107; display:none;"><img
                                                src="/assets/images/event/timeline-corner-g-7.png" class=""
                                                alt="角球"/></span> <span aria-haspopup="true" class="timeLineGoal"
                                                                        title="75' - 第1个进球 - 克里斯蒂亚诺•罗纳尔多  (尤文图斯) - 射门"
                                                                        style="left:83%;z-index:108; "><img
                                                src="/assets/images/event/gg.png" class="" alt="进球"/></span> <span
                                                aria-haspopup="true" class="timeLineGoal"
                                                title="90+2' - 第2个进球 - 冈扎罗•伊瓜因  (尤文图斯) - 射门"
                                                style="right: -8px;margin-right:5px;;z-index:109; "><img
                                                src="/assets/images/event/gg.png" class="" alt="进球"/></span> <img
                                                src="/assets/images/icon_HT.png" class="timeLineHT"/>
                                        </div>
                                        <div class="row">
                                            <div class="small-12 columns">
                                                <table width="100%" class="live-list-table">
                                                    <thead>
                                                    <tr>
                                                        <th colspan="2" class="text-center">
                                                            半
                                                            <img src="/assets/images/icon_corner.png" width="16"
                                                                 alt="角球" title="角球" class="MT-3"/>
                                                            全
                                                        </th>
                                                        <th colspan="2" class="text-center">
                                                            半
                                                            <img src="/assets/images/icon_goal.png" width="16" alt="进球"
                                                                 title="进球"/>
                                                            全
                                                        </th>
                                                        <th class="text-center"><img src="/assets/images/icon_chart.png"
                                                                                     width="14" class="VM MT-3"/> 盘口走势
                                                        </th>
                                                    </tr>
                                                    </thead>
                                                    <tbody>
                                                    <tr>
                                                        <td class="text-center" width="70">5 : 0</td>
                                                        <td class="text-center" width="70">6 : 2</td>
                                                        <td class="text-center" width="70">0 : 0</td>
                                                        <td class="text-center" width="70">0 : 2</td>
                                                        <td class="text-center">
                                                            <a href="javascript:void(0)">
                                                                -0.5 / 3.0 / 10.5 <img
                                                                    src="/assets/images/icon_corner.png" alt="角球"
                                                                    width="14" class="MT-3"/> </a>
                                                        </td>
                                                    </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="small-2 columns text-center">
                                        <div class="analysisTeamImg">
                                            <img src='https://s.besget.com/team/b/2687.png'/></div>
                                        <h3 class="analysisTeamName blue-color"><a href="/team/178"
                                                                                   class="blue-color font-bold"
                                                                                   target="_blank">尤文图斯</a></h3>
                                    </div>
                                </div>
                            </div>
                            <div class="analysisNav">
                                <ul class="small-block-grid-9">
                                    <li><a href="/race_sp/701326" class="  ">四合一数据</a></li>
                                    <li><a href="/race_fx/701326" class=" ">比赛分析</a></li>
                                    <li><a href="/race/701326">比赛信息</a></li>
                                    <li><a href="/race_ss/701326">数据统计</a></li>
                                    <li><a href="/race_baijia/701326">百家指数</a></li>
                                    <li><a href="/race_xc/701326" class="active">现场数据</a></li>
                                    <li><a href="/race_kz/701326">进球快照</a></li>
                                    <li><a href="/race_jfb/701326">积分榜</a></li>
                                    <li><a href="/live/ouguan/701326.html" target="_blank">直播集锦</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="small-12 medium-9 columns">
                            <div class="panel panel-l">
                                <div class="panel-heading">
                                    <h3>现场数据</h3>
                                </div>
                                <div class="panel-body">
                                    <div id="shezheng"
                                         style="min-width:600px;height:400px; margin-bottom:20px; border-bottom:4px solid #eee;"></div>
                                    <div id="shepian"
                                         style="min-width:600px;height:400px; margin-bottom:20px; border-bottom:4px solid #eee;"></div>
                                    <div id="danger"
                                         style="min-width:600px;height:400px; margin-bottom:20px; border-bottom:4px solid #eee;"></div>
                                    <div id="attack" style="min-width:600px;height:400px;"></div>
                                </div>
                            </div>
                            <div class="panel">
                                <div class="panel-body">
                                    <div class="row">
                                        <div class="small-6 columns">
                                            <p class="text-center MBTitle"><span class="label radius">首发阵容</span></p>
                                            <div class="row">
                                                <div class="small-6 columns text-right">
                                                    <dl>
                                                        <dt><b><i>主队</i></b></dt>
                                                        <dd class="MBMini">
                                                            L Hradecky
                                                        </dd>
                                                        <dd class="MBMini">
                                                            亚历山大•德拉戈维奇
                                                        </dd>
                                                        <dd class="MBMini">
                                                            达利•辛克赫拉芬
                                                        </dd>
                                                        <dd class="MBMini">
                                                            拉尔斯•本德
                                                        </dd>
                                                        <dd class="MBMini">
                                                            斯文•本德
                                                        </dd>
                                                        <dd class="MBMini">
                                                            阿兰吉斯
                                                        </dd>
                                                        <dd class="MBMini">
                                                            <span class="red-color">66'</span>
                                                            <img src="/assets/images/event/hs.png" width="18">
                                                            卡里姆•贝拉拉比
                                                        </dd>
                                                        <dd class="MBMini">
                                                            <span class="red-color">66'</span>
                                                            <img src="/assets/images/event/hs.png" width="18">
                                                            Kerem Demirbay
                                                        </dd>
                                                        <dd class="MBMini">
                                                            Moussa Diaby
                                                        </dd>
                                                        <dd class="MBMini">
                                                            凯•哈维茨
                                                        </dd>
                                                        <dd class="MBMini">
                                                            <span class="red-color">82'</span>
                                                            <img src="/assets/images/event/hs.png" width="18">
                                                            卢卡斯•阿拉里奥
                                                        </dd>
                                                    </dl>
                                                </div>
                                                <div class="small-6 columns text-left">
                                                    <dl>
                                                        <dt><b><i>客队</i></b></dt>
                                                        <dd class="MBMini">
                                                            吉安鲁吉•布冯
                                                        </dd>
                                                        <dd class="MBMini">
                                                            达席尔瓦•达尼洛
                                                        </dd>
                                                        <dd class="MBMini">
                                                            丹尼尔•鲁加尼
                                                        </dd>
                                                        <dd class="MBMini">
                                                            马蒂亚•德西利奥
                                                        </dd>
                                                        <dd class="MBMini">
                                                            M Demiral
                                                        </dd>
                                                        <dd class="MBMini">
                                                            阿德里安•拉比奥
                                                            <span class="red-color">85'</span>
                                                            <img src="/assets/images/event/gs.png" width="18">
                                                        </dd>
                                                        <dd class="MBMini">
                                                            费德里科•贝尔纳代斯基
                                                            <span class="red-color">66'</span>
                                                            <img src="/assets/images/event/gs.png" width="18">
                                                        </dd>
                                                        <dd class="MBMini">
                                                            胡安•吉列尔莫•夸德拉多
                                                            <span class="red-color">90'</span>
                                                            <img src="/assets/images/event/gs.png" width="18">
                                                        </dd>
                                                        <dd class="MBMini">
                                                            米拉勒姆•皮亚尼奇
                                                        </dd>
                                                        <dd class="MBMini">
                                                            克里斯蒂亚诺•罗纳尔多
                                                            <span class="red-color">75'</span>
                                                            <img src="/assets/images/event/gg.png" width="18">
                                                        </dd>
                                                        <dd class="MBMini">
                                                            冈扎罗•伊瓜因
                                                            <span class="red-color">90'</span>
                                                            <img src="/assets/images/event/gg.png" width="18">
                                                        </dd>
                                                    </dl>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="small-6 columns">
                                            <p class="text-center MBTitle"><span
                                                    class="label secondary radius">替补阵容</span></p>
                                            <div class="row">
                                                <div class="small-6 columns text-right">
                                                    <dl>
                                                        <dd class="MBMini">
                                                            拉玛赞•奥兹坎
                                                        </dd>
                                                        <dd class="MBMini">
                                                            博格斯•温德尔
                                                        </dd>
                                                        <dd class="MBMini">
                                                            乔那森•塔赫
                                                        </dd>
                                                        <dd class="MBMini">
                                                            帕纳约蒂斯•雷索斯
                                                        </dd>
                                                        <dd class="MBMini">
                                                            <span class="red-color">66'</span>
                                                            <img src="/assets/images/event/hs.png" width="18">
                                                            尤利安•鲍姆加特林格
                                                        </dd>
                                                        <dd class="MBMini">
                                                            <span class="red-color">82'</span>
                                                            <img src="/assets/images/event/hs.png" width="18">
                                                            凯文•福兰德
                                                        </dd>
                                                        <dd class="MBMini">
                                                            <span class="red-color">66'</span>
                                                            <img src="/assets/images/event/hs.png" width="18">
                                                            列昂•贝利
                                                        </dd>
                                                    </dl>
                                                </div>
                                                <div class="small-6 columns text-left">
                                                    <dl>
                                                        <dd class="MBMini">
                                                            沃伊切赫•什琴斯尼
                                                        </dd>
                                                        <dd class="MBMini">
                                                            罗博•阿莱士•桑德罗
                                                        </dd>
                                                        <dd class="MBMini">
                                                            莱昂纳多•博努奇
                                                        </dd>
                                                        <dd class="MBMini">
                                                            布莱斯•马图伊迪
                                                            <span class="red-color">85'</span>
                                                            <img src="/assets/images/event/gs.png" width="18">
                                                        </dd>
                                                        <dd class="MBMini">
                                                            M Portanova
                                                        </dd>
                                                        <dd class="MBMini">
                                                            西莫内•穆拉托雷
                                                            <span class="red-color">90'</span>
                                                            <img src="/assets/images/event/gs.png" width="18">
                                                        </dd>
                                                        <dd class="MBMini">
                                                            保罗•迪巴拉
                                                            <span class="red-color">66'</span>
                                                            <img src="/assets/images/event/gs.png" width="18">
                                                        </dd>
                                                    </dl>
                                                </div>
                                            </div>
                                        </div>

                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="small-12 medium-3 columns">
                            <div class="panel score-bar-con" id="race_data_pct">
                                <div class="panel-heading">
                                    全场数据
                                </div>
                                <div class="panel-body">
                                    <div class="score-bar-item">
                                        <h5>射正球门</h5>
                                        <div class="row">
                                            <div class="small-2 text-center columns">0</div>
                                            <div class="small-8 text-center columns">
                                                <div class="progress">
                                                    <span class="meter" style="width:0%"></span>
                                                </div>
                                            </div>

                                            <div class="small-2 text-center columns">2</div>
                                        </div>

                                    </div>
                                    <div class="score-bar-item">
                                        <h5>射偏球门</h5>
                                        <div class="row">
                                            <div class="small-2 text-center columns">11</div>
                                            <div class="small-8 text-center columns">
                                                <div class="progress small-12 radius">
                                                    <span class="meter" style="width: 84%"></span>
                                                </div>
                                            </div>

                                            <div class="small-2 text-center columns">2</div>
                                        </div>

                                    </div>
                                    <div class="score-bar-item">
                                        <h5>危险进攻</h5>
                                        <div class="row">
                                            <div class="small-2 text-center columns">56</div>
                                            <div class="small-8 text-center columns">
                                                <div class="progress">
                                                    <span class="meter" style="width: 70%"></span>
                                                </div>
                                            </div>
                                            <div class="small-2 text-center columns">24</div>
                                        </div>
                                    </div>
                                    <div class="score-bar-item">
                                        <h5>进攻</h5>
                                        <div class="row">
                                            <div class="small-2 text-center columns">127</div>
                                            <div class="small-8 text-center columns">
                                                <div class="progress">
                                                    <span class="meter" style="width: 56%"></span>
                                                </div>
                                            </div>
                                            <div class="small-2 text-center columns">96</div>
                                        </div>

                                    </div>

                                    <div class="score-bar-item">
                                        <h5>球权</h5>
                                        <div class="row">
                                            <div class="small-2 text-center columns">57%</div>
                                            <div class="small-8 text-center columns">
                                                <div class="progress">
                                                    <span class="meter" style="width: 57%"></span>
                                                </div>
                                            </div>
                                            <div class="small-2 text-center columns">43%</div>
                                        </div>
                                    </div>

                                </div>
                            </div>

                            <div class="panel score-bar-con" id="race_data_pct">
                                <div class="panel-heading">
                                    半场数据
                                </div>
                                <div class="panel-body">
                                    <div class="score-bar-item">
                                        <h5>射正球门</h5>
                                        <div class="row">
                                            <div class="small-2 text-center columns">0</div>
                                            <div class="small-8 text-center columns">
                                                <div class="progress">
                                                    <span class="meter" style="width:0%"></span>
                                                </div>
                                            </div>

                                            <div class="small-2 text-center columns">0</div>
                                        </div>

                                    </div>
                                    <div class="score-bar-item">
                                        <h5>射偏球门</h5>
                                        <div class="row">
                                            <div class="small-2 text-center columns">10</div>
                                            <div class="small-8 text-center columns">
                                                <div class="progress small-12 radius">
                                                    <span class="meter" style="width: 90%"></span>
                                                </div>
                                            </div>

                                            <div class="small-2 text-center columns">1</div>
                                        </div>

                                    </div>
                                    <div class="score-bar-item">
                                        <h5>危险进攻</h5>
                                        <div class="row">
                                            <div class="small-2 text-center columns">32</div>
                                            <div class="small-8 text-center columns">
                                                <div class="progress">
                                                    <span class="meter" style="width: 76%"></span>
                                                </div>
                                            </div>
                                            <div class="small-2 text-center columns">10</div>
                                        </div>
                                    </div>
                                    <div class="score-bar-item">
                                        <h5>进攻</h5>
                                        <div class="row">
                                            <div class="small-2 text-center columns">41</div>
                                            <div class="small-8 text-center columns">
                                                <div class="progress">
                                                    <span class="meter" style="width: 43%"></span>
                                                </div>
                                            </div>
                                            <div class="small-2 text-center columns">54</div>
                                        </div>

                                    </div>

                                    <div class="score-bar-item">
                                        <h5>球权</h5>
                                        <div class="row">
                                            <div class="small-2 text-center columns">62%</div>
                                            <div class="small-8 text-center columns">
                                                <div class="progress">
                                                    <span class="meter" style="width: 62%"></span>
                                                </div>
                                            </div>
                                            <div class="small-2 text-center columns">38%</div>
                                        </div>
                                    </div>

                                </div>
                            </div>
                            <ul class="pricing-table" id="race_events">
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/e.png" width="18"/>

                                    全场后得分 - 0-2
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/gs.png" width="18"/>

                                    90+3' - 换人 - 西莫内•穆拉托雷 换 胡安•吉列尔莫•夸德拉多 (尤文图斯)
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/gg.png" width="18"/>

                                    90+2' - 第2个进球 - 冈扎罗•伊瓜因 (尤文图斯) - 射门
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/it.png" width="18"/>

                                    下半场补时：4 分钟
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/gs.png" width="18"/>

                                    85' - 换人 - 布莱斯•马图伊迪 换 阿德里安•拉比奥 (尤文图斯)
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/hs.png" width="18"/>

                                    82' - 换人 - 凯文•福兰德 换 卢卡斯•阿拉里奥 (勒沃库森)
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:1进球数70:00 - 79:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:1角球数70:00 - 79:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0 罚牌 70:00 - 79:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/gg.png" width="18"/>

                                    75' - 第1个进球 - 克里斯蒂亚诺•罗纳尔多 (尤文图斯) - 射门
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/gc.png" width="18"/>

                                    74' - 第8角球 - 尤文图斯
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0进球数60:00 - 69:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0角球数60:00 - 69:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0 罚牌 60:00 - 69:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/gs.png" width="18"/>

                                    66' - 换人 - 保罗•迪巴拉 换 费德里科•贝尔纳代斯基 (尤文图斯)
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/hs.png" width="18"/>

                                    66' - 换人 - 列昂•贝利 换 卡里姆•贝拉拉比 (勒沃库森)
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/hs.png" width="18"/>

                                    66' - 换人 - 尤利安•鲍姆加特林格 换 Kerem Demirbay (勒沃库森)
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0进球数50:00 - 59:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    1:1角球数50:00 - 59:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0 罚牌 50:00 - 59:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/hc.png" width="18"/>

                                    56' - 第7角球 - 勒沃库森
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/gc.png" width="18"/>

                                    53' - 第6角球 - 尤文图斯
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0进球数40:00 - 49:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    2:0角球数40:00 - 49:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0 罚牌 40:00 - 49:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/h.png" width="18"/>

                                    上半场后得分 - 0-0
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    44' - 首先达到5个角球 - 勒沃库森
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/hc.png" width="18"/>

                                    44' - 第5角球 - 勒沃库森
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/hc.png" width="18"/>

                                    41' - 第4角球 - 勒沃库森
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0进球数30:00 - 39:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    1:0角球数30:00 - 39:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0 罚牌 30:00 - 39:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    34' - 首先达到3个角球 - 勒沃库森
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/hc.png" width="18"/>

                                    34' - 第3角球 - 勒沃库森
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0进球数20:00 - 29:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0角球数20:00 - 29:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0 罚牌 20:00 - 29:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0进球数10:00 - 19:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    2:0角球数10:00 - 19:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0 罚牌 10:00 - 19:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/hc.png" width="18"/>

                                    18' - 第2角球 - 勒沃库森
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/hc.png" width="18"/>

                                    17' - 第1角球 - 勒沃库森
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0进球数00:00 - 09:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0角球数00:00 - 09:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/d.png" width="18"/>

                                    0:0 罚牌 00:00 - 09:59
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/cd.png" width="18"/>

                                    场地：良好
                                </li>
                                <li class="bullet-item text-left">
                                    <img src="/assets/images/event/tq.png" width="18"/>

                                    天气：良好
                                </li>
                            </ul>
                        </div>
                    </div>

                    <script type="text/javascript" src="/assets/vendor/highcharts/highcharts.js"></script>
                    <script type="text/javascript" src="/assets/js/var_highcharts.js?_=3"></script>

                    <script>
                        function draw_half_line(highcharts_obj) {
                            var half_race_path_attr = {
                                'stroke-width': 1,
                                stroke: '#ccc',
                                dashstyle: 'dash'
                            };
                            var half_race_path_MY = 47;
                            var half_race_path_LY = 327;

                            var sz_xStart = highcharts_obj.xAxis[0].toPixels(45);
                            highcharts_obj.renderer.path(['M', sz_xStart, half_race_path_MY, 'L', sz_xStart, half_race_path_LY]).attr(half_race_path_attr).add();
                        }

                        $(document).ready(function () {

                            shezheng_chart_options = $.extend({}, goal_chart_options);
                            shezheng_chart_options.title = {"text": "射正球门 0 : 2"};
                            shezheng_chart_options.yAxis.title = {"text": "次数"};
                            shezheng_chart_options.series = [
                                {
                                    'name': '勒沃库森',
                                    'color': '#E45050',
                                    'data': [{
                                        "x": 0,
                                        "y": 0,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 16,
                                        "y": 0,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 17,
                                        "y": 0,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 33,
                                        "y": 0,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 40,
                                        "y": 0,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 44,
                                        "y": 0,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 55,
                                        "y": 0,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }],
                                    'lineWidth': 1,
                                    'states': {
                                        'lineWidth': 1.5
                                    }
                                },
                                {
                                    'name': '尤文图斯',
                                    'color': '#10AF80',
                                    'data': [{
                                        "x": 0,
                                        "y": 0,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 52,
                                        "y": 0,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "0",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 73,
                                        "y": 0,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "0",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 74,
                                        "y": 1,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 74,
                                        "y": 1,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_goal20x20.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "0",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 91,
                                        "y": 2,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 91,
                                        "y": 2,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_goal20x20.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "0",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }],
                                    'lineWidth': 1,
                                    'states': {
                                        'lineWidth': 1.5
                                    }
                                }
                            ];

                            $('#shezheng').css('min-width', $('#trend').width() - 40);
                            $('#shezheng').highcharts(shezheng_chart_options);

                            draw_half_line($('#shezheng').highcharts());


                            var shepian_chart_options = $.extend({}, goal_chart_options);
                            shepian_chart_options.title = {"text": "射偏球门 11 : 2"};
                            shepian_chart_options.yAxis.title = {"text": "次数"};
                            shepian_chart_options.series = [
                                {
                                    'name': '勒沃库森',
                                    'color': '#E45050',
                                    'data': [{
                                        "x": 0,
                                        "y": 0,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 4,
                                        "y": 1,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 9,
                                        "y": 2,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 10,
                                        "y": 3,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 14,
                                        "y": 4,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 14,
                                        "y": 5,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 16,
                                        "y": 5,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 17,
                                        "y": 5,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 17,
                                        "y": 6,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 33,
                                        "y": 6,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 34,
                                        "y": 7,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 40,
                                        "y": 7,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "1",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 40,
                                        "y": 8,
                                        "marker": {"radius": 2},
                                        "info": "1",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 40,
                                        "y": 8,
                                        "marker": {"radius": 2},
                                        "info": "1",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 43,
                                        "y": 9,
                                        "marker": {"radius": 2},
                                        "info": "1",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 44,
                                        "y": 9,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "1",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 44,
                                        "y": 10,
                                        "marker": {"radius": 2},
                                        "info": "1",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 55,
                                        "y": 10,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "1",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 88,
                                        "y": 11,
                                        "marker": {"radius": 2},
                                        "info": "2",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }],
                                    'lineWidth': 1,
                                    'states': {
                                        'lineWidth': 1.5
                                    }
                                },
                                {
                                    'name': '尤文图斯',
                                    'color': '#10AF80',
                                    'data': [{
                                        "x": 0,
                                        "y": 0,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 35,
                                        "y": 1,
                                        "marker": {"radius": 2},
                                        "info": "7",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 52,
                                        "y": 1,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "10",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 66,
                                        "y": 2,
                                        "marker": {"radius": 2},
                                        "info": "10",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 73,
                                        "y": 2,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "10",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 74,
                                        "y": 2,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_goal20x20.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "10",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 91,
                                        "y": 2,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_goal20x20.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "11",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }],
                                    'lineWidth': 1,
                                    'states': {
                                        'lineWidth': 1.5
                                    }
                                }
                            ];
                            $('#shepian').css('min-width', $('#trend').width() - 40);
                            $('#shepian').highcharts(shepian_chart_options);

                            draw_half_line($('#shepian').highcharts());

                            var shepian_chart_options = $.extend({}, goal_chart_options);
                            shepian_chart_options.title = {"text": "危险进攻 56 : 24"};
                            shepian_chart_options.series = [
                                {
                                    'name': '勒沃库森',
                                    'color': '#E45050',
                                    'data': [{
                                        "x": 0,
                                        "y": 0,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 1,
                                        "y": 1,
                                        "marker": {"radius": 2},
                                        "info": "2",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 3,
                                        "y": 2,
                                        "marker": {"radius": 2},
                                        "info": "2",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 4,
                                        "y": 3,
                                        "marker": {"radius": 2},
                                        "info": "2",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 4,
                                        "y": 4,
                                        "marker": {"radius": 2},
                                        "info": "2",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 6,
                                        "y": 5,
                                        "marker": {"radius": 2},
                                        "info": "2",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 9,
                                        "y": 6,
                                        "marker": {"radius": 2},
                                        "info": "2",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 9,
                                        "y": 7,
                                        "marker": {"radius": 2},
                                        "info": "2",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 12,
                                        "y": 8,
                                        "marker": {"radius": 2},
                                        "info": "4",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 13,
                                        "y": 9,
                                        "marker": {"radius": 2},
                                        "info": "4",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 13,
                                        "y": 10,
                                        "marker": {"radius": 2},
                                        "info": "4",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 14,
                                        "y": 11,
                                        "marker": {"radius": 2},
                                        "info": "4",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 16,
                                        "y": 12,
                                        "marker": {"radius": 2},
                                        "info": "4",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 16,
                                        "y": 12,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "4",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 16,
                                        "y": 13,
                                        "marker": {"radius": 2},
                                        "info": "4",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 17,
                                        "y": 13,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "4",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 17,
                                        "y": 14,
                                        "marker": {"radius": 2},
                                        "info": "4",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 17,
                                        "y": 15,
                                        "marker": {"radius": 2},
                                        "info": "4",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 17,
                                        "y": 16,
                                        "marker": {"radius": 2},
                                        "info": "4",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 17,
                                        "y": 17,
                                        "marker": {"radius": 2},
                                        "info": "4",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 19,
                                        "y": 18,
                                        "marker": {"radius": 2},
                                        "info": "5",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 33,
                                        "y": 18,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "5",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 34,
                                        "y": 19,
                                        "marker": {"radius": 2},
                                        "info": "5",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 37,
                                        "y": 20,
                                        "marker": {"radius": 2},
                                        "info": "7",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 37,
                                        "y": 21,
                                        "marker": {"radius": 2},
                                        "info": "7",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 39,
                                        "y": 22,
                                        "marker": {"radius": 2},
                                        "info": "7",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 40,
                                        "y": 23,
                                        "marker": {"radius": 2},
                                        "info": "7",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 40,
                                        "y": 23,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "7",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 40,
                                        "y": 24,
                                        "marker": {"radius": 2},
                                        "info": "7",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 40,
                                        "y": 25,
                                        "marker": {"radius": 2},
                                        "info": "7",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 40,
                                        "y": 26,
                                        "marker": {"radius": 2},
                                        "info": "7",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 43,
                                        "y": 27,
                                        "marker": {"radius": 2},
                                        "info": "10",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 43,
                                        "y": 28,
                                        "marker": {"radius": 2},
                                        "info": "10",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 44,
                                        "y": 28,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "10",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 44,
                                        "y": 29,
                                        "marker": {"radius": 2},
                                        "info": "10",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 44,
                                        "y": 30,
                                        "marker": {"radius": 2},
                                        "info": "10",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 44,
                                        "y": 31,
                                        "marker": {"radius": 2},
                                        "info": "10",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 45,
                                        "y": 32,
                                        "marker": {"radius": 2},
                                        "info": "10",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 47,
                                        "y": 33,
                                        "marker": {"radius": 2},
                                        "info": "11",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 47,
                                        "y": 34,
                                        "marker": {"radius": 2},
                                        "info": "11",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 54,
                                        "y": 35,
                                        "marker": {"radius": 2},
                                        "info": "19",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 55,
                                        "y": 35,
                                        "marker": {"radius": 2},
                                        "info": "19",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 55,
                                        "y": 35,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "19",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 55,
                                        "y": 36,
                                        "marker": {"radius": 2},
                                        "info": "19",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 58,
                                        "y": 37,
                                        "marker": {"radius": 2},
                                        "info": "20",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 60,
                                        "y": 38,
                                        "marker": {"radius": 2},
                                        "info": "20",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 60,
                                        "y": 39,
                                        "marker": {"radius": 2},
                                        "info": "20",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 60,
                                        "y": 40,
                                        "marker": {"radius": 2},
                                        "info": "20",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 63,
                                        "y": 41,
                                        "marker": {"radius": 2},
                                        "info": "21",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 70,
                                        "y": 42,
                                        "marker": {"radius": 2},
                                        "info": "22",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 71,
                                        "y": 43,
                                        "marker": {"radius": 2},
                                        "info": "22",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 71,
                                        "y": 44,
                                        "marker": {"radius": 2},
                                        "info": "22",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 77,
                                        "y": 45,
                                        "marker": {"radius": 2},
                                        "info": "23",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 78,
                                        "y": 46,
                                        "marker": {"radius": 2},
                                        "info": "24",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 78,
                                        "y": 47,
                                        "marker": {"radius": 2},
                                        "info": "24",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 78,
                                        "y": 48,
                                        "marker": {"radius": 2},
                                        "info": "24",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 83,
                                        "y": 49,
                                        "marker": {"radius": 2},
                                        "info": "24",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 86,
                                        "y": 50,
                                        "marker": {"radius": 2},
                                        "info": "24",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 86,
                                        "y": 51,
                                        "marker": {"radius": 2},
                                        "info": "24",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 88,
                                        "y": 52,
                                        "marker": {"radius": 2},
                                        "info": "24",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 88,
                                        "y": 53,
                                        "marker": {"radius": 2},
                                        "info": "24",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 88,
                                        "y": 54,
                                        "marker": {"radius": 2},
                                        "info": "24",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 88,
                                        "y": 55,
                                        "marker": {"radius": 2},
                                        "info": "24",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 90,
                                        "y": 56,
                                        "marker": {"radius": 2},
                                        "info": "24",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }],
                                    'lineWidth': 1,
                                    'states': {
                                        'lineWidth': 1.5
                                    }
                                },
                                {
                                    'name': '尤文图斯',
                                    'color': '#10AF80',
                                    'data': [{
                                        "x": 0,
                                        "y": 0,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 0,
                                        "y": 1,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 1,
                                        "y": 2,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 10,
                                        "y": 3,
                                        "marker": {"radius": 2},
                                        "info": "7",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 12,
                                        "y": 4,
                                        "marker": {"radius": 2},
                                        "info": "7",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 18,
                                        "y": 5,
                                        "marker": {"radius": 2},
                                        "info": "17",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 34,
                                        "y": 6,
                                        "marker": {"radius": 2},
                                        "info": "19",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 35,
                                        "y": 7,
                                        "marker": {"radius": 2},
                                        "info": "19",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 43,
                                        "y": 8,
                                        "marker": {"radius": 2},
                                        "info": "26",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 43,
                                        "y": 10,
                                        "marker": {"radius": 2},
                                        "info": "26",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 46,
                                        "y": 11,
                                        "marker": {"radius": 2},
                                        "info": "32",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 49,
                                        "y": 12,
                                        "marker": {"radius": 2},
                                        "info": "34",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 50,
                                        "y": 13,
                                        "marker": {"radius": 2},
                                        "info": "34",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 52,
                                        "y": 14,
                                        "marker": {"radius": 2},
                                        "info": "34",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 52,
                                        "y": 14,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "34",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 52,
                                        "y": 15,
                                        "marker": {"radius": 2},
                                        "info": "34",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 52,
                                        "y": 16,
                                        "marker": {"radius": 2},
                                        "info": "34",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 53,
                                        "y": 17,
                                        "marker": {"radius": 2},
                                        "info": "34",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 53,
                                        "y": 18,
                                        "marker": {"radius": 2},
                                        "info": "34",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 54,
                                        "y": 19,
                                        "marker": {"radius": 2},
                                        "info": "34",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 57,
                                        "y": 20,
                                        "marker": {"radius": 2},
                                        "info": "36",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 58,
                                        "y": 20,
                                        "marker": {"radius": 2},
                                        "info": "36",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 61,
                                        "y": 21,
                                        "marker": {"radius": 2},
                                        "info": "40",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 66,
                                        "y": 22,
                                        "marker": {"radius": 2},
                                        "info": "41",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 73,
                                        "y": 23,
                                        "marker": {"radius": 2},
                                        "info": "44",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 73,
                                        "y": 23,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "44",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 74,
                                        "y": 23,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_goal20x20.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "44",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 77,
                                        "y": 24,
                                        "marker": {"radius": 2},
                                        "info": "45",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 91,
                                        "y": 24,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_goal20x20.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "56",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }],
                                    'lineWidth': 1,
                                    'states': {
                                        'lineWidth': 1.5
                                    }
                                }
                            ];
                            $('#danger').css('min-width', $('#trend').width() - 40);
                            $('#danger').highcharts(shepian_chart_options);

                            draw_half_line($('#danger').highcharts());

                            var shepian_chart_options = $.extend({}, goal_chart_options);
                            shepian_chart_options.title = {"text": "进攻 127 : 96"};
                            shepian_chart_options.series = [
                                {
                                    'name': '勒沃库森',
                                    'color': '#E45050',
                                    'data': [{
                                        "x": 0,
                                        "y": 0,
                                        "marker": {"radius": 2},
                                        "info": "1",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 0,
                                        "y": 1,
                                        "marker": {"radius": 2},
                                        "info": "1",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 1,
                                        "y": 2,
                                        "marker": {"radius": 2},
                                        "info": "2",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 1,
                                        "y": 3,
                                        "marker": {"radius": 2},
                                        "info": "2",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 1,
                                        "y": 4,
                                        "marker": {"radius": 2},
                                        "info": "2",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 1,
                                        "y": 4,
                                        "marker": {"radius": 2},
                                        "info": "2",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 4,
                                        "y": 5,
                                        "marker": {"radius": 2},
                                        "info": "5",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 4,
                                        "y": 6,
                                        "marker": {"radius": 2},
                                        "info": "5",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 4,
                                        "y": 7,
                                        "marker": {"radius": 2},
                                        "info": "5",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 4,
                                        "y": 8,
                                        "marker": {"radius": 2},
                                        "info": "6",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 8,
                                        "y": 9,
                                        "marker": {"radius": 2},
                                        "info": "16",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 8,
                                        "y": 10,
                                        "marker": {"radius": 2},
                                        "info": "18",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 9,
                                        "y": 11,
                                        "marker": {"radius": 2},
                                        "info": "19",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 9,
                                        "y": 12,
                                        "marker": {"radius": 2},
                                        "info": "19",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 10,
                                        "y": 13,
                                        "marker": {"radius": 2},
                                        "info": "21",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 11,
                                        "y": 14,
                                        "marker": {"radius": 2},
                                        "info": "23",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 11,
                                        "y": 15,
                                        "marker": {"radius": 2},
                                        "info": "24",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 11,
                                        "y": 16,
                                        "marker": {"radius": 2},
                                        "info": "24",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 12,
                                        "y": 17,
                                        "marker": {"radius": 2},
                                        "info": "28",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 12,
                                        "y": 18,
                                        "marker": {"radius": 2},
                                        "info": "28",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 13,
                                        "y": 19,
                                        "marker": {"radius": 2},
                                        "info": "28",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 13,
                                        "y": 20,
                                        "marker": {"radius": 2},
                                        "info": "28",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 13,
                                        "y": 21,
                                        "marker": {"radius": 2},
                                        "info": "28",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 13,
                                        "y": 22,
                                        "marker": {"radius": 2},
                                        "info": "28",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 15,
                                        "y": 23,
                                        "marker": {"radius": 2},
                                        "info": "38",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 16,
                                        "y": 24,
                                        "marker": {"radius": 2},
                                        "info": "38",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 16,
                                        "y": 25,
                                        "marker": {"radius": 2},
                                        "info": "38",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 16,
                                        "y": 25,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "38",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 17,
                                        "y": 25,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "38",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 18,
                                        "y": 26,
                                        "marker": {"radius": 2},
                                        "info": "44",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 19,
                                        "y": 27,
                                        "marker": {"radius": 2},
                                        "info": "44",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 33,
                                        "y": 27,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "44",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 36,
                                        "y": 28,
                                        "marker": {"radius": 2},
                                        "info": "47",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 37,
                                        "y": 29,
                                        "marker": {"radius": 2},
                                        "info": "47",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 37,
                                        "y": 30,
                                        "marker": {"radius": 2},
                                        "info": "47",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 37,
                                        "y": 31,
                                        "marker": {"radius": 2},
                                        "info": "47",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 38,
                                        "y": 32,
                                        "marker": {"radius": 2},
                                        "info": "47",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 39,
                                        "y": 33,
                                        "marker": {"radius": 2},
                                        "info": "47",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 39,
                                        "y": 34,
                                        "marker": {"radius": 2},
                                        "info": "47",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 40,
                                        "y": 35,
                                        "marker": {"radius": 2},
                                        "info": "48",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 40,
                                        "y": 35,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "48",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 41,
                                        "y": 36,
                                        "marker": {"radius": 2},
                                        "info": "49",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 42,
                                        "y": 37,
                                        "marker": {"radius": 2},
                                        "info": "49",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 43,
                                        "y": 38,
                                        "marker": {"radius": 2},
                                        "info": "54",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 44,
                                        "y": 38,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "54",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 44,
                                        "y": 39,
                                        "marker": {"radius": 2},
                                        "info": "54",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 45,
                                        "y": 40,
                                        "marker": {"radius": 2},
                                        "info": "54",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 45,
                                        "y": 41,
                                        "marker": {"radius": 2},
                                        "info": "54",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 45,
                                        "y": 42,
                                        "marker": {"radius": 2},
                                        "info": "54",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 46,
                                        "y": 43,
                                        "marker": {"radius": 2},
                                        "info": "56",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 46,
                                        "y": 44,
                                        "marker": {"radius": 2},
                                        "info": "56",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 46,
                                        "y": 45,
                                        "marker": {"radius": 2},
                                        "info": "56",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 47,
                                        "y": 46,
                                        "marker": {"radius": 2},
                                        "info": "56",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 47,
                                        "y": 48,
                                        "marker": {"radius": 2},
                                        "info": "56",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 51,
                                        "y": 49,
                                        "marker": {"radius": 2},
                                        "info": "60",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 51,
                                        "y": 50,
                                        "marker": {"radius": 2},
                                        "info": "60",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 54,
                                        "y": 51,
                                        "marker": {"radius": 2},
                                        "info": "66",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 54,
                                        "y": 52,
                                        "marker": {"radius": 2},
                                        "info": "66",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 55,
                                        "y": 52,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "66",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 55,
                                        "y": 53,
                                        "marker": {"radius": 2},
                                        "info": "66",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 56,
                                        "y": 54,
                                        "marker": {"radius": 2},
                                        "info": "66",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 56,
                                        "y": 55,
                                        "marker": {"radius": 2},
                                        "info": "67",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 57,
                                        "y": 56,
                                        "marker": {"radius": 2},
                                        "info": "70",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 58,
                                        "y": 57,
                                        "marker": {"radius": 2},
                                        "info": "72",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 58,
                                        "y": 58,
                                        "marker": {"radius": 2},
                                        "info": "72",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 59,
                                        "y": 59,
                                        "marker": {"radius": 2},
                                        "info": "72",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 59,
                                        "y": 60,
                                        "marker": {"radius": 2},
                                        "info": "72",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 59,
                                        "y": 61,
                                        "marker": {"radius": 2},
                                        "info": "72",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 60,
                                        "y": 62,
                                        "marker": {"radius": 2},
                                        "info": "72",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 60,
                                        "y": 63,
                                        "marker": {"radius": 2},
                                        "info": "72",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 60,
                                        "y": 64,
                                        "marker": {"radius": 2},
                                        "info": "72",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 60,
                                        "y": 65,
                                        "marker": {"radius": 2},
                                        "info": "72",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 61,
                                        "y": 66,
                                        "marker": {"radius": 2},
                                        "info": "72",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 61,
                                        "y": 67,
                                        "marker": {"radius": 2},
                                        "info": "72",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 61,
                                        "y": 68,
                                        "marker": {"radius": 2},
                                        "info": "72",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 61,
                                        "y": 69,
                                        "marker": {"radius": 2},
                                        "info": "73",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 62,
                                        "y": 70,
                                        "marker": {"radius": 2},
                                        "info": "73",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 62,
                                        "y": 71,
                                        "marker": {"radius": 2},
                                        "info": "73",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 62,
                                        "y": 72,
                                        "marker": {"radius": 2},
                                        "info": "73",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 62,
                                        "y": 73,
                                        "marker": {"radius": 2},
                                        "info": "73",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 62,
                                        "y": 74,
                                        "marker": {"radius": 2},
                                        "info": "73",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 63,
                                        "y": 75,
                                        "marker": {"radius": 2},
                                        "info": "73",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 63,
                                        "y": 76,
                                        "marker": {"radius": 2},
                                        "info": "73",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 63,
                                        "y": 76,
                                        "marker": {"radius": 2},
                                        "info": "73",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 64,
                                        "y": 77,
                                        "marker": {"radius": 2},
                                        "info": "73",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 67,
                                        "y": 78,
                                        "marker": {"radius": 2},
                                        "info": "78",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 67,
                                        "y": 79,
                                        "marker": {"radius": 2},
                                        "info": "78",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 67,
                                        "y": 80,
                                        "marker": {"radius": 2},
                                        "info": "78",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 68,
                                        "y": 81,
                                        "marker": {"radius": 2},
                                        "info": "79",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 68,
                                        "y": 82,
                                        "marker": {"radius": 2},
                                        "info": "79",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 69,
                                        "y": 83,
                                        "marker": {"radius": 2},
                                        "info": "79",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 70,
                                        "y": 84,
                                        "marker": {"radius": 2},
                                        "info": "80",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 70,
                                        "y": 85,
                                        "marker": {"radius": 2},
                                        "info": "82",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 70,
                                        "y": 86,
                                        "marker": {"radius": 2},
                                        "info": "82",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 71,
                                        "y": 87,
                                        "marker": {"radius": 2},
                                        "info": "82",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 71,
                                        "y": 88,
                                        "marker": {"radius": 2},
                                        "info": "82",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 71,
                                        "y": 89,
                                        "marker": {"radius": 2},
                                        "info": "82",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 71,
                                        "y": 90,
                                        "marker": {"radius": 2},
                                        "info": "82",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 72,
                                        "y": 91,
                                        "marker": {"radius": 2},
                                        "info": "82",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 72,
                                        "y": 92,
                                        "marker": {"radius": 2},
                                        "info": "83",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 72,
                                        "y": 93,
                                        "marker": {"radius": 2},
                                        "info": "83",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 74,
                                        "y": 94,
                                        "marker": {"radius": 2},
                                        "info": "85",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 76,
                                        "y": 95,
                                        "marker": {"radius": 2},
                                        "info": "87",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 76,
                                        "y": 96,
                                        "marker": {"radius": 2},
                                        "info": "87",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 77,
                                        "y": 97,
                                        "marker": {"radius": 2},
                                        "info": "87",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 77,
                                        "y": 98,
                                        "marker": {"radius": 2},
                                        "info": "87",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 77,
                                        "y": 99,
                                        "marker": {"radius": 2},
                                        "info": "89",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 78,
                                        "y": 100,
                                        "marker": {"radius": 2},
                                        "info": "89",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 78,
                                        "y": 101,
                                        "marker": {"radius": 2},
                                        "info": "89",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 78,
                                        "y": 102,
                                        "marker": {"radius": 2},
                                        "info": "89",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 78,
                                        "y": 103,
                                        "marker": {"radius": 2},
                                        "info": "90",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 79,
                                        "y": 104,
                                        "marker": {"radius": 2},
                                        "info": "90",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 80,
                                        "y": 105,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 82,
                                        "y": 106,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 82,
                                        "y": 107,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 82,
                                        "y": 108,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 82,
                                        "y": 109,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 83,
                                        "y": 110,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 83,
                                        "y": 111,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 83,
                                        "y": 112,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 83,
                                        "y": 112,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 83,
                                        "y": 113,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 83,
                                        "y": 114,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 85,
                                        "y": 115,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 85,
                                        "y": 116,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 85,
                                        "y": 117,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 85,
                                        "y": 117,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 85,
                                        "y": 118,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 86,
                                        "y": 119,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 87,
                                        "y": 120,
                                        "marker": {"radius": 2},
                                        "info": "92",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 88,
                                        "y": 121,
                                        "marker": {"radius": 2},
                                        "info": "93",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 88,
                                        "y": 121,
                                        "marker": {"radius": 2},
                                        "info": "93",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 89,
                                        "y": 122,
                                        "marker": {"radius": 2},
                                        "info": "95",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 90,
                                        "y": 123,
                                        "marker": {"radius": 2},
                                        "info": "95",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 90,
                                        "y": 124,
                                        "marker": {"radius": 2},
                                        "info": "95",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 90,
                                        "y": 125,
                                        "marker": {"radius": 2},
                                        "info": "95",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 90,
                                        "y": 126,
                                        "marker": {"radius": 2},
                                        "info": "95",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }, {
                                        "x": 94,
                                        "y": 127,
                                        "marker": {"radius": 2},
                                        "info": "96",
                                        "name": "\u5c24\u6587\u56fe\u65af"
                                    }],
                                    'lineWidth': 1,
                                    'states': {
                                        'lineWidth': 1.5
                                    }
                                },
                                {
                                    'name': '尤文图斯',
                                    'color': '#10AF80',
                                    'data': [{
                                        "x": 0,
                                        "y": 1,
                                        "marker": {"radius": 2},
                                        "info": "0",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 1,
                                        "y": 2,
                                        "marker": {"radius": 2},
                                        "info": "1",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 1,
                                        "y": 3,
                                        "marker": {"radius": 2},
                                        "info": "4",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 2,
                                        "y": 4,
                                        "marker": {"radius": 2},
                                        "info": "4",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 3,
                                        "y": 5,
                                        "marker": {"radius": 2},
                                        "info": "4",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 4,
                                        "y": 6,
                                        "marker": {"radius": 2},
                                        "info": "8",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 5,
                                        "y": 7,
                                        "marker": {"radius": 2},
                                        "info": "8",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 7,
                                        "y": 9,
                                        "marker": {"radius": 2},
                                        "info": "8",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 7,
                                        "y": 10,
                                        "marker": {"radius": 2},
                                        "info": "8",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 7,
                                        "y": 11,
                                        "marker": {"radius": 2},
                                        "info": "8",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 7,
                                        "y": 12,
                                        "marker": {"radius": 2},
                                        "info": "8",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 7,
                                        "y": 13,
                                        "marker": {"radius": 2},
                                        "info": "8",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 8,
                                        "y": 14,
                                        "marker": {"radius": 2},
                                        "info": "8",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 8,
                                        "y": 15,
                                        "marker": {"radius": 2},
                                        "info": "8",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 8,
                                        "y": 16,
                                        "marker": {"radius": 2},
                                        "info": "8",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 8,
                                        "y": 17,
                                        "marker": {"radius": 2},
                                        "info": "9",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 8,
                                        "y": 18,
                                        "marker": {"radius": 2},
                                        "info": "9",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 8,
                                        "y": 19,
                                        "marker": {"radius": 2},
                                        "info": "10",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 10,
                                        "y": 20,
                                        "marker": {"radius": 2},
                                        "info": "12",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 10,
                                        "y": 21,
                                        "marker": {"radius": 2},
                                        "info": "12",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 11,
                                        "y": 22,
                                        "marker": {"radius": 2},
                                        "info": "13",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 11,
                                        "y": 23,
                                        "marker": {"radius": 2},
                                        "info": "13",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 11,
                                        "y": 24,
                                        "marker": {"radius": 2},
                                        "info": "15",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 12,
                                        "y": 25,
                                        "marker": {"radius": 2},
                                        "info": "16",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 12,
                                        "y": 26,
                                        "marker": {"radius": 2},
                                        "info": "16",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 12,
                                        "y": 27,
                                        "marker": {"radius": 2},
                                        "info": "16",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 12,
                                        "y": 28,
                                        "marker": {"radius": 2},
                                        "info": "16",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 14,
                                        "y": 29,
                                        "marker": {"radius": 2},
                                        "info": "22",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 14,
                                        "y": 30,
                                        "marker": {"radius": 2},
                                        "info": "22",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 14,
                                        "y": 32,
                                        "marker": {"radius": 2},
                                        "info": "22",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 15,
                                        "y": 33,
                                        "marker": {"radius": 2},
                                        "info": "22",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 15,
                                        "y": 34,
                                        "marker": {"radius": 2},
                                        "info": "22",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 15,
                                        "y": 35,
                                        "marker": {"radius": 2},
                                        "info": "22",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 15,
                                        "y": 36,
                                        "marker": {"radius": 2},
                                        "info": "22",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 15,
                                        "y": 37,
                                        "marker": {"radius": 2},
                                        "info": "22",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 15,
                                        "y": 38,
                                        "marker": {"radius": 2},
                                        "info": "22",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 18,
                                        "y": 39,
                                        "marker": {"radius": 2},
                                        "info": "25",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 18,
                                        "y": 40,
                                        "marker": {"radius": 2},
                                        "info": "25",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 18,
                                        "y": 41,
                                        "marker": {"radius": 2},
                                        "info": "25",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 18,
                                        "y": 42,
                                        "marker": {"radius": 2},
                                        "info": "25",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 18,
                                        "y": 44,
                                        "marker": {"radius": 2},
                                        "info": "25",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 34,
                                        "y": 46,
                                        "marker": {"radius": 2},
                                        "info": "27",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 35,
                                        "y": 47,
                                        "marker": {"radius": 2},
                                        "info": "27",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 40,
                                        "y": 48,
                                        "marker": {"radius": 2},
                                        "info": "34",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 41,
                                        "y": 49,
                                        "marker": {"radius": 2},
                                        "info": "35",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 42,
                                        "y": 50,
                                        "marker": {"radius": 2},
                                        "info": "37",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 43,
                                        "y": 51,
                                        "marker": {"radius": 2},
                                        "info": "37",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 43,
                                        "y": 52,
                                        "marker": {"radius": 2},
                                        "info": "37",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 43,
                                        "y": 54,
                                        "marker": {"radius": 2},
                                        "info": "37",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 43,
                                        "y": 54,
                                        "marker": {"radius": 2},
                                        "info": "38",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 45,
                                        "y": 55,
                                        "marker": {"radius": 2},
                                        "info": "42",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 45,
                                        "y": 56,
                                        "marker": {"radius": 2},
                                        "info": "42",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 48,
                                        "y": 57,
                                        "marker": {"radius": 2},
                                        "info": "48",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 48,
                                        "y": 57,
                                        "marker": {"radius": 2},
                                        "info": "48",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 49,
                                        "y": 58,
                                        "marker": {"radius": 2},
                                        "info": "48",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 49,
                                        "y": 59,
                                        "marker": {"radius": 2},
                                        "info": "48",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 50,
                                        "y": 60,
                                        "marker": {"radius": 2},
                                        "info": "48",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 51,
                                        "y": 61,
                                        "marker": {"radius": 2},
                                        "info": "50",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 52,
                                        "y": 62,
                                        "marker": {"radius": 2},
                                        "info": "50",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 52,
                                        "y": 62,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "50",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 53,
                                        "y": 63,
                                        "marker": {"radius": 2},
                                        "info": "50",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 53,
                                        "y": 64,
                                        "marker": {"radius": 2},
                                        "info": "50",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 53,
                                        "y": 65,
                                        "marker": {"radius": 2},
                                        "info": "50",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 54,
                                        "y": 66,
                                        "marker": {"radius": 2},
                                        "info": "50",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 56,
                                        "y": 67,
                                        "marker": {"radius": 2},
                                        "info": "54",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 57,
                                        "y": 68,
                                        "marker": {"radius": 2},
                                        "info": "55",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 57,
                                        "y": 69,
                                        "marker": {"radius": 2},
                                        "info": "55",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 57,
                                        "y": 70,
                                        "marker": {"radius": 2},
                                        "info": "55",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 57,
                                        "y": 71,
                                        "marker": {"radius": 2},
                                        "info": "56",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 57,
                                        "y": 72,
                                        "marker": {"radius": 2},
                                        "info": "56",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 61,
                                        "y": 73,
                                        "marker": {"radius": 2},
                                        "info": "68",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 64,
                                        "y": 74,
                                        "marker": {"radius": 2},
                                        "info": "77",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 65,
                                        "y": 75,
                                        "marker": {"radius": 2},
                                        "info": "77",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 66,
                                        "y": 76,
                                        "marker": {"radius": 2},
                                        "info": "77",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 66,
                                        "y": 77,
                                        "marker": {"radius": 2},
                                        "info": "77",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 66,
                                        "y": 78,
                                        "marker": {"radius": 2},
                                        "info": "77",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 67,
                                        "y": 79,
                                        "marker": {"radius": 2},
                                        "info": "80",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 69,
                                        "y": 80,
                                        "marker": {"radius": 2},
                                        "info": "83",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 70,
                                        "y": 81,
                                        "marker": {"radius": 2},
                                        "info": "84",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 70,
                                        "y": 82,
                                        "marker": {"radius": 2},
                                        "info": "85",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 72,
                                        "y": 83,
                                        "marker": {"radius": 2},
                                        "info": "91",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 73,
                                        "y": 84,
                                        "marker": {"radius": 2},
                                        "info": "93",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 73,
                                        "y": 84,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_corner14x14.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "93",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 73,
                                        "y": 85,
                                        "marker": {"radius": 2},
                                        "info": "93",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 74,
                                        "y": 86,
                                        "marker": {"radius": 2},
                                        "info": "94",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 74,
                                        "y": 87,
                                        "marker": {"radius": 2},
                                        "info": "94",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 74,
                                        "y": 87,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_goal20x20.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "94",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 77,
                                        "y": 88,
                                        "marker": {"radius": 2},
                                        "info": "98",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 77,
                                        "y": 89,
                                        "marker": {"radius": 2},
                                        "info": "98",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 78,
                                        "y": 90,
                                        "marker": {"radius": 2},
                                        "info": "102",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 79,
                                        "y": 91,
                                        "marker": {"radius": 2},
                                        "info": "104",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 87,
                                        "y": 92,
                                        "marker": {"radius": 2},
                                        "info": "119",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 88,
                                        "y": 93,
                                        "marker": {"radius": 2},
                                        "info": "120",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 89,
                                        "y": 95,
                                        "marker": {"radius": 2},
                                        "info": "121",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 91,
                                        "y": 96,
                                        "marker": {"radius": 2},
                                        "info": "126",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }, {
                                        "x": 91,
                                        "y": 96,
                                        "marker": {
                                            "symbol": "url(\/assets\/images\/icon_goal20x20.png)",
                                            "width": 14,
                                            "height": 14
                                        },
                                        "info": "126",
                                        "name": "\u52d2\u6c83\u5e93\u68ee"
                                    }],
                                    'lineWidth': 1,
                                    'states': {
                                        'lineWidth': 1.5
                                    }
                                }
                            ];
                            $('#attack').css('min-width', $('#trend').width() - 40);
                            $('#attack').highcharts(shepian_chart_options);

                            draw_half_line($('#attack').highcharts());
                        });
                    </script>

    </main>


    <div class="pageFixedBar2 show-for-medium-up" id="pageFixedBar2">
        <!--
    <a href="javascript:void(0);" class="comBarImgClose" style="display: none;">关闭</a>
    <img src="/assets/images/icons/comBar.png" class="comBarImg" style="display: none;" />
    -->
        <a title="比赛评论" class="fixbarCommentBt" id="fixbarCommentBt"><img
                src="/assets/images/icons/comComment.jpg"/></a>
        <a href="https://www.dslanqiu.com" target="_blank" title="DS篮球" rel="nofollow"><img
                src="/assets/images/icons/comDSLQ.jpg"/></a>
        <a href="javascript:void(0);" title="" data-dropdown="wechatQRCode"
           data-options="align:left;is_hover:true; hover_timeout:500"><img src="/assets/images/icons/comPhone.jpg"/></a>
        <a href="//www.dszuqiu.com/contact" title=""><img src="/assets/images/icons/comChat.jpg"/></a>
        <a href="javascript:void(0);" id="backtotop" title="返回顶部"><img src="/assets/images/icons/comBackToTop.jpg"/></a>
        <div id="raceComment" class="raceComment">
            <div class="row">
                <div class="small-4 columns PL0 PR0">
                    <div class="raceCommentRaceList miniScroller">
                        <ul id="race_table" class="content">

                        </ul>
                    </div>
                </div>
                <div class="small-8 columns PL0 PR0">
                    <div class="raceCommentMain" id="raceCommentMain">

                    </div>
                </div>
            </div>
            <div class="raceAlertPopup">
                <h3>确定举报此条评论吗？</h3>
                <p>
                    <a id="report_confirm" href="javascript:report()" class="button tiny radius  MB0 MRTitle">确认</a> <a
                        id="report_cancel" href="javascript:void(0)" class="button tiny action radius MB0">取消</a>
                </p>
            </div>
            <div class="raceAlertPopupMask"></div>
        </div>
        <div id="wechatQRCode" data-dropdown-content class="f-dropdown content" aria-hidden="true" tabindex="-1">
            <img src="/assets/images/index/qrcode.png?_2"/>
            <span>扫码安装APP</span>
        </div>
    </div>

    <script>
        $(document).ready(function () {
            $('#backtotop').on('click', function () {
                $('body').scrollTo('#topBar', 300);
            });
        });
    </script>
    <script>
        if (typeof (DS_user) == "undefined") {
            var DS_user = {
                'is_logined': 1,
                'mobile_not_binded': 1
            };
        }
        if (typeof (DS_config) == "undefined") {
            var DS_config = {
                'is_corner_enabled': 1,
                'root_domain': '//www.dszuqiu.com',
                'base_path': '',
                'lang': 'cn'
            };
        }
    </script>

    <footer class="main-footer">
        <p class="MBTitle">
            声明：本网资讯仅供体育爱好者进行比赛浏览观看研究之用，任何人不得用于非法用途，否则责任自负。所有内容不得违反国家法律规定，如有违者本网有权随时予以删除，并保留与有关部门合作追究的权利。
        </p>
        <p class="MBTitle">
            商务合作QQ：<a target="_blank"
                      href="http://sighttp.qq.com/authd?IDKEY=c4c6bd5d3191bff4ef04095aafd88cac6ad52e1b1b4aeca3"
                      rel="nofollow"><img src="/assets/images/qqContact-b.png" class="qqActive" title="商务合作"
                                          width="20"/></a> |
            <a href="//www.dszuqiu.com/">足球比分</a> | <a href="//live.dszuqiu.com/corner">角球比分</a> | <a
                href="//www.dszuqiu.com/jczq">竞彩足球</a> | <a href="//www.dszuqiu.com/bjdc">北京单场</a> |
            <a href="//www.dszuqiu.com/about-us" rel="nofollow">关于我们</a> | <a href="//www.dszuqiu.com/contact"
                                                                              rel="nofollow">意见反馈</a> | Copyright &copy;
            2020 DSZUQIU.COM. All Rights Reserved. <a href="http://www.beian.miit.gov.cn">蜀ICP备14008209号</a></p>
        <div id="footerWechatQRCode" data-dropdown-content class="f-dropdown content" aria-hidden="true" tabindex="-1">
            <img src="/assets/images/wechatQRCode.jpg?_=2" width="60"/>
            <span>关注DS足球官方微信</span>
        </div>
    </footer>

</div>
<script>
    $(document).ready(function () {
        $('.topBarAccountLink').on('click', function () {
            $('#acountDrop').toggle();
        });
        $('.topBarAccount').hover(
            function () {
                $('#acountDropEn').show();
            },
            function () {
                $('#acountDropEn').hide();
            }
        );
        $('.fa-search').on('click', function (e) {
            var text = $('.searchField').val();
            if (text.length <= 0) return;
            jQuery("#data_search").submit();
        });
        $(document).mouseup(function (e) {
            var _con = $('#acountDrop');
            if (!_con.is(e.target) && _con.has(e.target).length === 0 && !$('.topBarAccount').is(e.target) && $('.topBarAccount').has(e.target).length === 0) {
                $('#acountDrop').hide();
            }
        });

        $('.iamNotAdClose').on('click', function (e) {
            e.preventDefault();
            if (confirm('VIP可关闭广告')) {
                window.location = "https://www.dszuqiu.com/user/vip";
            }
        });


        if (document.domain != 'www.ds' + 'zuqiu.com') {
            window.location.href = 'https://www.dszuqi' + 'u.com/';
        }


    });
</script>
<script src="/assets/js/app.min.js?_=13"></script>
</body>
</html>



"""
# print(wb_data.read())
# html = etree.HTML(wb_data.read())
# print(re.findall(wb_data.read()))
# print(html.xpath("//script"))


names = Selector(text=data).xpath("//script")[-5]
js_text = names.xpath("./text()").extract_first()
# print(names)
# print(js_text)
# print("---正则")
# print(re.findall(r"shepian_chart_options.series =.*?(?=,])",names))
# shepian_chart_options.title = {"text": "危险进攻 56 : 24"};
# patten = re.compile("data(.*)?]", re.S)
# datas = patten.findall(names)
#
# for d in datas:
#     print("-"*10)
# print(d)
# print(len(datas))

script_text = js2xml.parse(js_text, encoding='utf-8', debug=False)
script_tree = js2xml.pretty_print(script_text)
selector = etree.HTML(script_tree)
# print(selector)
# print(js2xml.pretty_print(script_text))
# print(selector.xpath("//property[@name='data']"))
data_s = selector.xpath("//property[@name='data']")
dics = []
for xys in data_s:
    xs = xys.xpath(".//property[@name='x']/number/@value")
    ys = xys.xpath(".//property[@name='y']/number/@value")
    print("x------------------------")
    print(xs)
    print("y--------------------------")
    print(ys)
    # print(xs)
    dic = dict(map(lambda x, y: [x, y], xs, ys))
    dics.append(dic)
print(dics[1])
print(len(dics))  # 2个求队的正门  偏门 危险进攻 进攻/格式x:y


def find_current_data(datas, current_time):
    # 如果有这个时刻的数据，直接查找
    # 没有的话找到这个时间的前一个时刻

    #  1 有这个时间段的数据直接返回
    #  2 没有找到比他时间大的前一个值
    #  3 他比最后一个还要大直接返回最后一个
    current_data = datas.get(str(current_time))
    if current_data is None:
        keys = list(datas.keys())
        values = list(datas.values())
        if current_time > int(keys[len(keys) - 1]):  # 比最后一个大
            current_data = values[len(values) - 1]
        else:
            for i in keys:
                if (int(i) > int(current_time)):
                    print(values[keys.index(i) - 1])  # 查找前一时间段的数据
                    current_data = values[keys.index(i) - 1]
                    break
    else:
        current_data = int(datas.get(str(current_time)))
    return int(current_data)
print("测试查找数据--------------")
print(dics[2])
print(find_current_data(dics[2], 88))

# 清洗数据
# 1 射正球门  2 射偏球门  3 危险进攻  4 进攻
# 6 分钟处理
home_zheng = find_current_data(dics[0], 6)
away_zheng = find_current_data(dics[1], 6)
home_pian = find_current_data(dics[2],6)
away_pian = find_current_data(dics[3],6)
home_risk = find_current_data(dics[4], 6)
away_risk = find_current_data(dics[5], 6)
home_attack = find_current_data(dics[6], 6)
away_attack = find_current_data(dics[7], 6)

# 危比  如果为0按0.5算
def zero_to_half(a):
    if a==0:
        return 0.5
    else:
        return float(a)
print("危攻比测试------------------------")
risk_rate = round(zero_to_half(home_risk)/zero_to_half(away_risk),2)
print(home_risk)
print(away_risk)
print(risk_rate)

print("攻比测试------------------------")

attack_rate = round(zero_to_half(home_attack)/zero_to_half(away_attack),2)
print(home_attack)
print(away_attack)
print(attack_rate)

print("主客正----------------------------")
print(home_zheng)
print(away_zheng)


print("主客总-----------------------------")
home_total = home_zheng+home_pian
away_total = away_zheng+away_pian
print(home_total)
print(away_total)
total_cha = home_total - away_total
print(total_cha)

total_attack_rate = round(zero_to_half(home_total)/zero_to_half(away_total),2)
print(total_attack_rate)
print("6主6客计算----------------")
# 净胜球 + 盘口 - 6分钟净胜球
