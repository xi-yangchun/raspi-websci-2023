<?php
//クラスを呼び出してオブジェクトを作成
$objDateTime = new DateTime();
$targ_hour=13;
$targ_min=26;
 
//format()メソッドで現在日時を出力
echo $objDateTime->format('Y-m-d')."<br/>\n";//現在日付 2020-01-01
echo $objDateTime->format('H:i:s')."<br/>\n";//現在時間 01:01:01
echo $objDateTime->format('Y-m-d H:i:s')."<br/>\n";//現在日時 2020-01-01 01:01:01

while(true){
    sleep(1);
    //fix hour in2 JST
    $hour_now=(int)date('H')+9;
    $min_now=(int)date('i');
    if($hour_now==$targ_hour && $min_now==$targ_min){
        break;
    }
}
echo 'alarm!!!!';
?>