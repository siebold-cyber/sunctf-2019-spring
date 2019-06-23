<?php
error_reporting(0);

mb_language("uni");
mb_internal_encoding("utf-8");
mb_http_input("utf-8");
mb_http_output("utf-8");

if (isset($_GET['source'])) {
  show_source(__FILE__);
  exit();
}

$dsn = 'mysql:host=' . getenv('MYSQL_HOST') . ';dbname=' . getenv('MYSQL_DATABASE');
$user = getenv('MYSQL_USER');
$password = getenv('MYSQL_PASSWORD');

$body = file_get_contents('php://input');
$json = json_decode($body, true);
$bookData = array();

if (isset($json) && isset($json['req'])) {
  $req = $json['req'];

  if ($req === 'fetchAll') {
    $sql = "SELECT * FROM books";
  } else if ($req === 'getBooks') {
    $name = $json['name'];
    $name = '%' . $name . '%';
    $sql = "SELECT * FROM books WHERE name LIKE '$name'";
  }

  $dbh = new PDO($dsn, $user, $password);

  $sth = $dbh->query($sql);

  while($row = $sth->fetch(PDO::FETCH_ASSOC)) {
    $bookData[]=array(
      'id'=>$row['id'],
      'name'=>$row['name'],
      'author'=>$row['author'],
      'ISBN'=>$row['ISBN']
    );
  }

  $sth = null;
  $dbh = null;
} else {
  $bookData = "Access Denied";
}

header('Content-Type: application/json');
echo json_encode(['content' => $bookData]);
