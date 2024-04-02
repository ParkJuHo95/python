package kr.co.aiai.high;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.app.Activity;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;

public class ActivityLocationManager extends Activity implements LocationListener {
    LocationManager lm;
    TextView tv;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_location_manager);
        Button btn = findViewById(R.id.btn);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                tv.setText("");
            }
        });
        Button btn1 = findViewById(R.id.btn1);
        btn1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    String textWrite = (String)tv.getText();
                    FileOutputStream fileoutputstream = openFileOutput("babo.txt", MODE_PRIVATE);
//                    File file = new File("babo.txt");
//                    FileReader fr = new FileReader(file);
//                    String oldTxt = "";
//                    int ch;
//                    while ((ch = fr.read()) != -1) {
//                        oldTxt += ch;
//                    }
//                    String newTxt = oldTxt + textWrite;
//                    fileoutputstream.write(newTxt.getBytes());
                    fileoutputstream.write(textWrite.getBytes());
                    fileoutputstream.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });

        tv = findViewById(R.id.tv);
        lm = (LocationManager) getSystemService(LOCATION_SERVICE);
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (ActivityCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            return;
        }
        lm.requestLocationUpdates(LocationManager.GPS_PROVIDER, 1000, 5, this);
    }

    @Override
    protected void onPause() {
        super.onPause();
        lm.removeUpdates(this);
    }

    @Override
    public void onLocationChanged(Location location) {
        String text = "lat:" + location.getLatitude() + "\t" + "lng:" + location.getLongitude() + "\n";
        tv.setText(text + tv.getText());
    }
}