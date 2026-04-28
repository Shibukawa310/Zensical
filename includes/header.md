<div style="display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-top: 1px solid #eee; border-bottom: 1px solid #eee; margin: 20px 0; color: #555; font-size: 0.9em;">
  <span><strong>ID:</strong> {{ page.meta.ID }}</span>
  <span><strong>Version:</strong> {{ page.meta.Version }}</span>
  <span><strong>Status:</strong> 
    <span class="status-tag status-{{ page.meta.Status | lower }}" style="padding: 2px 8px; border-radius: 4px; font-weight: bold; color: white; text-transform: uppercase; font-size: 0.85em;">
      {{ page.meta.Status }}
    </span>
  </span>
  <span><strong>Maj:</strong> {{ page.meta['Last Updated'] }}</span>
</div>
