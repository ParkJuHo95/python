package kr.co.aiai.high;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.hardware.SensorListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class ActivitySensorManagerPaint extends AppCompatActivity implements SensorListener {
    TextView tv;
    SensorManager sensormanager;
    ViewMe viewme;
    float[] values = new float[6];

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        viewme = new ViewMe(this);
        setContentView(viewme);
        sensormanager = (SensorManager) getSystemService(SENSOR_SERVICE);
    }

    @Override
    protected void onResume() {
        sensormanager.registerListener(this, SensorManager.SENSOR_ALL);
        super.onResume();
    }
    @Override
    protected void onPause() {
        sensormanager.unregisterListener(this);
        super.onPause();
    }

    @Override
    public void onSensorChanged(int sensor, float[] values) {
        if (sensor == SensorManager.SENSOR_ORIENTATION) {
            String text = "";
            this.values[0] = values[0];
            this.values[1] = values[1];
            this.values[2] = values[2];
            this.values[3] = values[3];
            this.values[4] = values[4];
            this.values[5] = values[5];
            viewme.invalidate();        //있던 그림을 지우고 그림을 다시 그려라
        }
    }

    @Override
    public void onAccuracyChanged(int i, int i1) {

    }

    private class ViewMe extends View {

        public ViewMe(Context context) {
            super(context);
        }

        @Override
        protected void onDraw(Canvas canvas) {
            Paint paint = new Paint();
            paint.setColor(Color.RED);
            paint.setStrokeWidth(10);
            canvas.drawLine(500 + 20 * 0, 700 + values[0] * 3, 500 + 20 * 0, 800, paint);
            canvas.drawLine(500 + 20 * 1, 700 + values[1] * 3, 500 + 20 * 1, 800, paint);
            canvas.drawLine(500 + 20 * 2, 700 + values[2] * 3, 500 + 20 * 2, 800, paint);
            canvas.drawLine(500 + 20 * 3, 700 + values[3] * 3, 500 + 20 * 3, 800, paint);
            canvas.drawLine(500 + 20 * 4, 700 + values[4] * 3, 500 + 20 * 4, 800, paint);
            canvas.drawLine(500 + 20 * 5, 700 + values[5] * 3, 500 + 20 * 5, 800, paint);

            paint.setColor(Color.BLUE);
            paint.setTextSize(50);
            canvas.drawText(values[0] + "", 50, 200, paint);
            canvas.drawText(values[1] + "", 50, 200 + 50, paint);
            canvas.drawText(values[2] + "", 50, 200 + 110, paint);
            canvas.drawText(values[3] + "", 50, 200 + 170, paint);
            canvas.drawText(values[4] + "", 50, 200 + 230, paint);
            canvas.drawText(values[5] + "", 50, 200 + 290, paint);

            super.onDraw(canvas);
        }
    }
}