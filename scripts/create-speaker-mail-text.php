<?php


$placeholders = array(
    '<SPEAKER_NAME>'       => 'Max',
    '<WEEKDAY_OF_MEETUP>'  => 'Thursday',
    '<NUMBER_OF_PEOPLE>'   => 'x',
    '<DATE_OF_MEETUP>'     => 'March 27th, 2019',
    '<CONTACT_MAIL>'       => '@@@',
    '<TWITTER_HANDLE>'     => '@WenEngAc',
    '<LOCATION>'           => 'Aachen',
    '<MOBILE_NUMBER>'      => '555-Nase',
    '<AUTHOR>'             => 'Niels',
    '<LINK-OF-MEETUP>'     => ''
);

$originContent = file_get_contents(__DIR__ . '/../SPEAKER_INFORMATION.md');

$mailText = $originContent;
    $mailText = strtr($mailText, $placeholders);

echo $mailText;
