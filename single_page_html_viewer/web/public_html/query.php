<?php
error_reporting(0);

if (isset($_GET['source'])) {
  show_source(__FILE__);
  exit();
}

$body = file_get_contents('php://input');
$json = json_decode($body, true);

if (isset($json) && isset($json['page'])) {
    $page = $json['page'];
    $content = file_get_contents($page);

    if (!$content) {
        $content = "<p>Not Found</p>\n";
    }
} else {
  $content = "<p>Access Denied</p>\n";
}

echo json_encode(['content' => $content]);
?>
