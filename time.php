<?php


$total = 0.0;
echo "Day | A | B | Combined\n";
for ($x=1; $x<12; $x++){
    $durationDay = 0;
    $day = str_pad($x, 2, "0", STR_PAD_LEFT);
    echo "{$day} |";
    $time = microtime(true);
    $command = "cat day{$day}.data.txt | python3 day{$day}a.py > /dev/null";
    exec($command);
    $duration = microtime(true) - $time;
    $total += $duration;

    $durationDay += $duration;
    echo "{$duration} | ";
    $time = microtime(true);
    $command = "cat day{$day}.data.txt | python3 day{$day}b.py > /dev/null";
    exec($command);
    $duration = microtime(true) - $time;
    $durationDay += $duration;
    $total += $duration;
    echo "{$duration} | {$durationDay}\n";;
}


echo "{$total}\n";