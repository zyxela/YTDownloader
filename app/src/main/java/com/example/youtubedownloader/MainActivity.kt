package com.example.youtubedownloader

import android.annotation.SuppressLint
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform

class MainActivity : AppCompatActivity() {
    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        if (! Python.isStarted())
            Python.start(AndroidPlatform(this))

        val pythonObj = Python.getInstance()
        val module = pythonObj.getModule("downloader")

        val str = module["main"]?.toString()
        findViewById<TextView>(R.id.txtv).text = str

    }
}